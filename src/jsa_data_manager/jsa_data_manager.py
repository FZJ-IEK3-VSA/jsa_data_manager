import pandas
import json
import pathlib
import csv
from jsa_data_manager.data_types import (
    TimeSeriesColumnEntryMetaData,
    SoftwareSource,
    DataSource,
    TimeSeriesFileMetaData,
    TimeStampColumnMetaData,
    DataSourceTypes,
    TimeSeriesStandards,
)
from jsa_data_manager.warning_and_error import CorruptedData, IncompleteData


class LoadProfileDataManager:
    def __init__(self) -> None:
        pass

    def read_meta_data_dictionary(self, path_to_meta_data: str) -> dict:
        string_path = str(path_to_meta_data)
        with open(string_path) as json_file:
            meta_data_dictionary = json.load(json_file)
        return meta_data_dictionary

    def _convert_meta_data_path_csv(self, path_to_meta_data: str | pathlib.Path) -> str:
        if isinstance(path_to_meta_data, str):
            path_to_meta_data = pathlib.Path(path_to_meta_data)
        path_to_meta_data_without_file_extension = path_to_meta_data.stem
        path_to_csv_data_str = str(path_to_meta_data_without_file_extension) + ".csv"
        path_to_csv_data = pathlib.Path(path_to_csv_data_str)
        if not path_to_csv_data.is_file():
            raise Exception("No csv file exists at: " + path_to_csv_data_str)
        return path_to_csv_data_str

    def read_to_data_frame(
        self, path_to_meta_data: str | pathlib.Path
    ) -> pandas.DataFrame:
        meta_data_dictionary = self.read_meta_data_dictionary(
            path_to_meta_data=path_to_meta_data
        )
        time_stamp_column_meta_data = self.get_time_stamp_column_meta_data(
            meta_data_dictionary=meta_data_dictionary
        )
        path_to_csv_file = self._convert_meta_data_path_csv(
            path_to_meta_data=path_to_meta_data
        )
        date_columns = [
            time_stamp_column_meta_data.start_column_name,
            time_stamp_column_meta_data.end_column_name,
        ]
        data_frame = pandas.read_csv(
            filepath_or_buffer=path_to_csv_file,
            delimiter=",",
            parse_dates=date_columns,
            index_col=time_stamp_column_meta_data.index_column_name,
        )
        return data_frame

    def read_to_dataclass(self, path_to_meta_data: str) -> TimeSeriesFileMetaData:
        meta_data_dictionary = self.read_meta_data_dictionary(
            path_to_meta_data=path_to_meta_data
        )
        time_stamp_column_meta_data = self.get_time_stamp_column_meta_data(
            meta_data_dictionary=meta_data_dictionary
        )
        date_columns = [
            time_stamp_column_meta_data.start_column_name,
            time_stamp_column_meta_data.end_column_name,
        ]

        path_to_csv_file = self._convert_meta_data_path_csv(
            path_to_meta_data=path_to_meta_data
        )
        data_frame = pandas.read_csv(
            filepath_or_buffer=path_to_csv_file,
            delimiter=meta_data_dictionary["delimiter"],
            parse_dates=date_columns,
            index_col=time_stamp_column_meta_data.index_column_name,
        )

        source_data = self.get_source_data(meta_data_dict=meta_data_dictionary)
        list_of_column_meta_data = []
        for column_meta_data in meta_data_dictionary["time_series_meta_data"][
            "column_list"
        ]:
            list_of_column_meta_data.append(
                TimeSeriesColumnEntryMetaData(**column_meta_data)
            )
        load_profile_meta_data = TimeSeriesFileMetaData(
            name=meta_data_dictionary["time_series_meta_data"]["name"],
            data_frame=data_frame,
            column_list=list_of_column_meta_data,
            software_run_data=source_data,
            data_format_standard=meta_data_dictionary["data_format_standard"],
            first_start_time=meta_data_dictionary["time_series_meta_data"][
                "first_start_time"
            ],
            last_end_time=meta_data_dictionary["time_series_meta_data"][
                "last_end_time"
            ],
            time_stamp_column_meta_data=time_stamp_column_meta_data,
        )
        return load_profile_meta_data

    def get_time_stamp_column_meta_data(
        self, meta_data_dictionary: dict[str, dict]
    ) -> TimeStampColumnMetaData:
        time_stamp_column_meta_data = TimeStampColumnMetaData(
            index_column_name=meta_data_dictionary["time_series_meta_data"][
                "time_stamp_column_meta_data"
            ]["index_column_name"],
            index_column_number=meta_data_dictionary["time_series_meta_data"][
                "time_stamp_column_meta_data"
            ]["index_column_number"],
            start_column_name=meta_data_dictionary["time_series_meta_data"][
                "time_stamp_column_meta_data"
            ]["start_column_name"],
            start_column_number=meta_data_dictionary["time_series_meta_data"][
                "time_stamp_column_meta_data"
            ]["start_column_number"],
            end_column_name=meta_data_dictionary["time_series_meta_data"][
                "time_stamp_column_meta_data"
            ]["end_column_name"],
            end_column_number=meta_data_dictionary["time_series_meta_data"][
                "time_stamp_column_meta_data"
            ]["end_column_number"],
        )
        return time_stamp_column_meta_data

    def get_list_of_time_series_column_meta_data(
        self, time_series_column_list: list[dict[str, str]]
    ) -> list[TimeSeriesColumnEntryMetaData]:
        list_of_time_series_meta_data = []
        for time_series_column_dict in time_series_column_list:

            if "description" in time_series_column_dict:
                description = time_series_column_dict["description"]
            else:
                description = None

            if "tags" in time_series_column_dict:
                tags = time_series_column_dict["tags"]
            else:
                tags = None

            if "min" in time_series_column_dict:

                min = time_series_column_dict["min"]
            else:
                min = None
            if "max" in time_series_column_dict:
                max = time_series_column_dict["max"]
            else:
                max = None
            list_of_time_series_meta_data.append(
                TimeSeriesColumnEntryMetaData(
                    column_number=time_series_column_dict["column_number"],
                    column_name=time_series_column_dict["column_name"],
                    unit=time_series_column_dict["unit"],
                    description=description,
                    tags=tags,
                    min=min,
                    max=max,
                )
            )
        return list_of_time_series_meta_data

    def get_source_data(
        self, meta_data_dict: dict[str, dict[str, str]]
    ) -> SoftwareSource | DataSource:
        if DataSourceTypes.DATA_SOURCE in meta_data_dict:
            source_meta_data = SoftwareSource(
                source_type=DataSourceTypes.DATA_SOURCE,
                source_name=meta_data_dict["source_name"],
                reference=meta_data_dict["reference"],
                guid=meta_data_dict["guid"],
            )
        elif DataSourceTypes.SOFTWARE_SOURCE in meta_data_dict:
            source_meta_data = SoftwareSource(
                source_type=DataSourceTypes.DATA_SOURCE,
                software_name=meta_data_dict["software_name"],
                version=meta_data_dict["version"],
                user_name=meta_data_dict["user_name"],
                guid=meta_data_dict["guid"],
            )
        else:
            raise IncompleteData("Expected Either")
        return source_meta_data

    def create_data_frame(self):
        pass

    def write_meta_data(
        self,
        name: str,
        data_frame: pandas.DataFrame,
        source_meta_data: SoftwareSource | DataSource,
        column_list: list[TimeSeriesColumnEntryMetaData],
        start_column_name: str = "start",
        end_column_name: str = "end",
        index_column_name: str = "index",
        delimiter=",",
    ) -> TimeSeriesFileMetaData:
        start_column_number = data_frame.columns.get_loc(start_column_name)
        end_column_number = data_frame.columns.get_loc(end_column_name)
        index_column_number = data_frame.columns.get_loc(index_column_name)
        time_stamp_column_meta_data = TimeStampColumnMetaData(
            index_column_number=index_column_number,
            index_column_name=index_column_name,
            start_column_name=start_column_name,
            start_column_number=start_column_number,
            end_column_name=end_column_name,
            end_column_number=end_column_number,
        )
        times_series_standard = TimeSeriesFileMetaData(
            name=name,
            data_frame=data_frame,
            time_stamp_column_meta_data=time_stamp_column_meta_data,
            column_list=column_list,
            source_meta_data=source_meta_data,
            delimiter=delimiter,
            times_series_standard=TimeSeriesStandards.V1_0,
        )
        return times_series_standard


class JSADataManager:
    def __init__(self) -> None:
        self.load_profile_data_manager: LoadProfileDataManager = (
            LoadProfileDataManager()
        )

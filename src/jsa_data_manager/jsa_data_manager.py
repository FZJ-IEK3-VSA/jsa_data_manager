import pandas
import json

from jsa_data_manager.data_types import (
    TimeSeriesColumnEntryMetaData,
    SoftwareRunData,
    TimeSeriesFileMetaData,
    TimeStampColumnMetaData,
)


# class DataManagerBase:
#     def read_csv_to_data_frame(self, path: str) -> pandas.DataFrame:
#         data_frame = pandas.read_csv(io=path)
#         return data_frame

#     def read_excel_to_data_frame(self, path: str) -> pandas.DataFrame:
#         data_frame = pandas.read_excel(io=path)
#         return data_frame


class LoadProfileDataManager:
    def __init__(self) -> None:
        pass

    def read_meta_data_dictionary(self, path_to_meta_data: str) -> dict:
        string_path = str(path_to_meta_data)
        with open(string_path) as json_file:
            meta_data_dictionary = json.load(json_file)
        return meta_data_dictionary

    def read_load_profile_data(
        self, path_to_data_frame: str, path_to_meta_data: str
    ) -> TimeSeriesFileMetaData:
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
        data_frame = pandas.read_csv(
            filepath_or_buffer=path_to_data_frame,
            delimiter=",",
            parse_dates=date_columns,
            index_col=time_stamp_column_meta_data.index_column_name,
        )

        software_run_data = SoftwareRunData(
            **meta_data_dictionary["time_series_meta_data"]["software_run_data"]
        )
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
            software_run_data=software_run_data,
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


class JSADataManager:
    def __init__(self) -> None:
        self.load_profile_data_manager: LoadProfileDataManager = (
            LoadProfileDataManager()
        )

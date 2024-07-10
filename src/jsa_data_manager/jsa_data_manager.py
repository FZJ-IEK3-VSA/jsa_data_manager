import csv
import getpass
import json
import pathlib
import uuid
import warnings

import pandas
from jsa_data_manager.data_types import (
    DataSource,
    DataSourceTypes,
    SoftwareSource,
    TimeSeriesColumnEntryMetaData,
    TimeSeriesFileMetaData,
    TimeSeriesFileMetaDataWODataFrame,
    TimeSeriesStandards,
    TimeStampColumnMetaData,
)
from jsa_data_manager.warning_and_error import CorruptedData, IncompleteData
from pydantic import BaseModel


class LoadProfileDataManager:
    def __init__(self) -> None:
        pass

    def read_meta_data_dictionary(self, path_to_meta_data: str) -> dict:
        string_path = str(path_to_meta_data)
        with open(string_path, encoding="utf-8") as json_file:
            meta_data_dictionary = json.load(json_file)
        return meta_data_dictionary

    def _convert_meta_data_path_csv(self, path_to_meta_data: str | pathlib.Path) -> str:
        if isinstance(path_to_meta_data, str):
            path_to_meta_data = pathlib.Path(path_to_meta_data)
        file_name_without_extension = path_to_meta_data.stem
        path_to_folder = path_to_meta_data.parent
        file_name_with_csv_extension = str(file_name_without_extension) + ".csv"
        path_to_csv_data_str = str(
            path_to_folder.joinpath(file_name_with_csv_extension)
        )
        path_to_csv_data = pathlib.Path(path_to_csv_data_str)
        if not path_to_csv_data.is_file():
            raise Exception("No csv file exists at: " + path_to_csv_data_str)
        return path_to_csv_data_str

    def read_meta_data_without_df(
        self, path_to_json: str | pathlib.Path
    ) -> TimeSeriesFileMetaDataWODataFrame:
        with open(str(path_to_json), encoding="utf-8") as file:
            json_dict = json.load(file)
            json_string = json.dumps(json_dict)
        time_series_file_meta_data_without_data_frame = (
            TimeSeriesFileMetaDataWODataFrame.model_validate_json(json_data=json_string)
        )
        return time_series_file_meta_data_without_data_frame

    def read_df(self, path_to_meta_data: str | pathlib.Path) -> pandas.DataFrame:
        meta_data = self.read_meta_data_without_df(path_to_json=str(path_to_meta_data))
        path_to_csv_file = self._convert_meta_data_path_csv(
            path_to_meta_data=path_to_meta_data
        )
        data_frame = pandas.read_csv(
            filepath_or_buffer=path_to_csv_file,
            delimiter=",",
            parse_dates=[
                meta_data.time_stamp_column_meta_data.start_column_name,
                meta_data.time_stamp_column_meta_data.end_column_name,
            ],
            index_col=meta_data.time_stamp_column_meta_data.index_column_name,
        )
        return data_frame

    def read_meta_data_class(
        self, path_to_meta_data: str | pathlib.Path
    ) -> pandas.DataFrame:
        meta_data = self.read_meta_data_without_df(path_to_json=str(path_to_meta_data))
        path_to_csv_file = self._convert_meta_data_path_csv(
            path_to_meta_data=path_to_meta_data
        )
        data_frame = pandas.read_csv(
            filepath_or_buffer=path_to_csv_file,
            delimiter=",",
            parse_dates=[
                meta_data.time_stamp_column_meta_data.start_column_name,
                meta_data.time_stamp_column_meta_data.end_column_name,
            ],
            index_col=meta_data.time_stamp_column_meta_data.index_column_name,
        )
        meta_data_with_df = TimeSeriesFileMetaData(
            data_frame=data_frame, **meta_data.model_dump()
        )
        return meta_data_with_df

    def write_time_series_meta_data_software(
        self,
        path_to_file: str,
        name: str,
        data_frame: pandas.DataFrame,
        software_name: str,
        software_version: str,
        column_list: list[TimeSeriesColumnEntryMetaData],
        time_stamp_column_meta_data: TimeStampColumnMetaData,
        delimiter=",",
    ):

        software_version_str = str(software_version)
        try:
            user_name = str(getpass.getuser())
        except:
            warnings.warn("Username could not be retrieved automatically")
            user_name = "Could not Get Username automatically"

        software_source = SoftwareSource(
            software_name=software_name,
            source_type=DataSourceTypes.SOFTWARE_SOURCE,
            version=software_version_str,
            user_name=user_name,
            guid=str(uuid.uuid4()),
        )
        times_series_standard = TimeSeriesFileMetaData(
            name=name,
            data_frame=data_frame,
            time_stamp_column_meta_data=time_stamp_column_meta_data,
            column_list=column_list,
            data_source=software_source,
            delimiter=delimiter,
            data_format_standard=TimeSeriesStandards.V1_0,
        )

        path_to_file_without_extension = pathlib.Path(path_to_file).joinpath(name)
        path_to_file_without_extension_str = str(path_to_file_without_extension)
        data_frame.to_csv(
            sep=",", path_or_buf=path_to_file_without_extension_str + ".csv"
        )
        meta_data_json_string = times_series_standard.model_dump_json()
        with open(
            path_to_file_without_extension_str + ".json", "w", encoding="utf-8"
        ) as file:
            json_dict = json.loads(s=meta_data_json_string)
            json.dump(obj=json_dict, fp=file)


class JSADataManager:
    def __init__(self) -> None:
        self.load_profile_data_manager: LoadProfileDataManager = (
            LoadProfileDataManager()
        )

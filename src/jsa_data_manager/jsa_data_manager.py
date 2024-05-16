import pandas
import json

from jsa_data_manager.data_types import (
    LoadProfileMetaData,
    LoadProfileMetaDataNonUniform,
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
    ) -> LoadProfileMetaData:
        meta_data_dictionary = self.read_meta_data_dictionary(
            path_to_meta_data=path_to_meta_data
        )

        date_columns = [
            meta_data_dictionary["field_names"]["start_time"],
            meta_data_dictionary["field_names"]["end_time"],
        ]
        data_frame = pandas.read_csv(
            filepath_or_buffer=path_to_data_frame,
            delimiter=",",
            parse_dates=date_columns,
        )
        load_profile_meta_data = LoadProfileMetaData(
            data_frame=data_frame,
            **meta_data_dictionary["data_type_specific_load_type"],
            # name=meta_data_dictionary["data_type_specific_load_type"]["name"],
            # first_start_time=meta_data_dictionary["data_type_specific_load_type"][
            #     "first_start_time"
            # ],
            # last_end_time=meta_data_dictionary["data_type_specific_load_type"][
            #     "last_end_time"
            # ],
            # total_energy=meta_data_dictionary["data_type_specific_load_type"][
            #     "total_energy"
            # ],
            # minimum_power=meta_data_dictionary["data_type_specific_load_type"][
            #     "minimum_power"
            # ],
            # maximum_power=meta_data_dictionary["data_type_specific_load_type"][
            #     "maximum_power"
            # ],
            # power_unit=meta_data_dictionary["data_type_specific_load_type"][
            #     "power_unit"
            # ],
            # energy_unit=meta_data_dictionary["data_type_specific_load_type"][
            #     "energy_unit"
            # ],
            # load_type=meta_data_dictionary["data_type_specific_load_type"]["load_type"],
            # step_duration=meta_data_dictionary["data_type_specific_load_type"][
            #     "step_duration"
            # ],
        )
        return load_profile_meta_data


class JSADataManager:
    def __init__(self) -> None:
        self.load_profile_data_manager: LoadProfileDataManager = (
            LoadProfileDataManager()
        )

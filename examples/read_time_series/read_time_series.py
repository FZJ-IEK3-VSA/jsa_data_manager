import datetime
import pathlib
import pandas
import numpy
from jsa_data_manager.jsa_data_manager import JSADataManager
from jsa_data_manager.data_types import TimeSeriesColumnEntryMetaData


jsa_data_manager = JSADataManager()
current_directory = pathlib.Path(__file__).parent.absolute()
path_to_json = current_directory.joinpath("Random Electricity Time Series.json")
# Returns only the meta data without the actual data frame
solo_meta_data = jsa_data_manager.load_profile_data_manager.read_meta_data_without_df(
    path_to_json
)
# csv file must have the same name the json file
# Returns the data frame without additional meta data, still considers the data types and column names
solo_df = jsa_data_manager.load_profile_data_manager.read_df(path_to_json)
# Returns a data class that contains all meta data in the json and the data frame as addtional attribute
meta_data_with_df = jsa_data_manager.load_profile_data_manager.read_meta_data_class(
    path_to_json
)

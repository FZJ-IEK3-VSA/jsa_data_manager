import datetime
import pathlib
import pandas
import numpy
from jsa_data_manager.jsa_data_manager import JSADataManager
from jsa_data_manager.data_types import (
    TimeSeriesColumnEntryMetaData,
    TimeStampColumnMetaData,
)


# Create a dummy test series to store
start_date_range = (
    pandas.date_range(
        start=datetime.datetime(year=2022, month=1, day=2, hour=0),
        end=datetime.datetime(year=2022, month=1, day=3, hour=0),
        freq="h",
    )
    .to_series(name="start")
    .reset_index(drop=True)
)
end_date_range = (
    pandas.date_range(
        start=datetime.datetime(year=2022, month=1, day=2, hour=1),
        end=datetime.datetime(year=2022, month=1, day=3, hour=1),
        freq="h",
    )
    .to_series(name="end")
    .reset_index(drop=True)
)

random_data = pandas.Series(
    numpy.random.rand(1, 25).squeeze(axis=0), name="Electricity Demand"
)
time_series_data_frame = pandas.concat(
    [start_date_range, end_date_range, random_data], axis=1
)
time_series_data_frame.index.name = "index"

# Write file and Meta Data
jsa_data_manager = JSADataManager()
# get path to folder where csv file and meta data json should be stored
current_directory = pathlib.Path(__file__).parent

start_column_name = "start"
end_column_name = "end"
start_column_number = time_series_data_frame.columns.get_loc(start_column_name) + 1
end_column_number = time_series_data_frame.columns.get_loc(end_column_name) + 1
time_stamp_column_meta_data = TimeStampColumnMetaData(
    index_column_number=0,
    index_column_name="index",
    start_column_number=1,
    start_column_name=start_column_name,
    end_column_number=2,
    end_column_name=end_column_name,
)


# name of the csv file and meta json only differ in the extension .csv and .json
jsa_data_manager.load_profile_data_manager.write_time_series_meta_data_software(
    path_to_file=current_directory,
    name="Random Electricity Time Series",
    data_frame=time_series_data_frame,
    software_name="Random Time Series Generator",
    software_version="1.0",
    column_list=[
        TimeSeriesColumnEntryMetaData(
            column_number=3,
            column_name="Electricity Demand",
            description="Electricity Demand",
            unit="kW",
        )
    ],
    time_stamp_column_meta_data=time_stamp_column_meta_data,
)

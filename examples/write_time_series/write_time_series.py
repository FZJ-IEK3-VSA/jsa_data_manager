####################################################################################
##   An example to show how to write a time_series_df to timeseries.csv           ##
##            and add meta data manually with the jsa_data_manager                ##
##                                                                                ##
##   a. Software case                                                             ##
##   b. ...  to be continued                                                      ##
##                                                                                ##
####################################################################################
# At the moment, only the "software case" is taken into account here. 
# This means: You have created a time_series_data_frame with RESkit or another ETHOS.Suite package, for example. 
# Various meta data can be added here with the *write_time_series_meta_data_software* function. 
# In this particular software case, this is the name of the software and its version. 
# Other cases will follow soon. For example, time series from external sources.

import datetime
import pathlib
import pandas
import numpy
from jsa_data_manager.jsa_data_manager import JSADataManager
from jsa_data_manager.data_types import TimeSeriesColumnEntryMetaData


# Create a dummy time_series_df 
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
    numpy.random.rand(1, 25).squeeze(axis=0), name="Electicity Demand"
)
#add all toghether to create the time_series_data_frame
time_series_data_frame = pandas.concat(
    [start_date_range, end_date_range, random_data], axis=1
)
time_series_data_frame.index.name = "index"


####################################################################################
##                               a. Software case                                 ##
####################################################################################

#adding your meta data 
jsa_data_manager = JSADataManager()
# get path to folder where csv file and meta data json should be stored
current_directory = pathlib.Path(__file__).parent
# name of the csv file and meta json only differ in the extension .csv and .json
jsa_data_manager.load_profile_data_manager.write_time_series_meta_data_software(
    path_to_file=current_directory,     #location whre our data will be stored
    name="Random Electricity Time Series",  #name of the file you create 
    data_frame=time_series_data_frame,  #dataframe you want to write/store
    software_name="Random Time Series Generator",       #could be fine or RESKit for example
    software_version="1.0",
    column_list=[                     #here you are adding your meta data!
        TimeSeriesColumnEntryMetaData(
            column_number=1,
            column_name="Electicity Demand",
            description="Electricity Demand",
            unit="kW",
            # TODO add TimeStampColumnMeta Data explicitly
        )
    ],
)

####################################################################################
##                      b. other applications... to be continued                  ##
####################################################################################
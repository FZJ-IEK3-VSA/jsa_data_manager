# Jülich System Analysis DataManager
This library can be used to read and write data and the corresponding Meta Data according to the  Meta data standard of the Jülich System Analysis Meta Data standard.
Currently only the meta data standard for the time series data is implemented. Further data types are in discussion.

# Installation of the jsa_data_manager
## 1. Clone jsa_papckage
```git clone https://jugit.fz-juelich.de/iek-3/shared-code/jsa_data_manager.git```

## 2. Deactivate base environment
permanent solution if you don't want the base env to activate automatically every time 
````conda config --set auto_activate_base false```
or simply
````conda deactivate```
**Importent step** else you might run into problems during installation of the package

## 3. Set up an environment
```conda env create -n jsa_data_manager_env --file environment.yml```
or update an existing environment
```conda env update -n testing_with julian --file environment.yml```

## 4. Activate your environment
```conda activate jsa_data_manager_env```

## 5. Install the papckage
```pip install -e .```

# Short package description
At the moment you can use this package:
## 1. To read in time series 
An example on how to use jsa_data_manager to read in your time series can be found here: *jsa_data_manager/examples/read_time_series/read_time_series.py*.
Example of the default format for a random timeseries.csv as input: *jsa_data_manager/examples/read_time_series/Random Electricity Time Series.csv*.
In *jsa_data_manager/examples/write_time_series/Random Electricity Time Series.json* you also find an example of default meta data structure.
**read_time_series.py** gives you the option of **a.** reading only meta data without times_series.csv, **b.** reading only your meta_data.json or **c.** reading both at the same time. In this case, the names should be the same as well as the storage location of the meta data and time series.

## 2. To write your time series and add the meta data
An example on how to use jsa_data_manager to write your time series + meta data can be found here: *jsa_data_manager/examples/write_time_series*.
**write_time_series.py** gives you the option to 
at the same time, add meta data to your time series and save your time_series_data_frame as a csv and the associated meta data in a destination folder. 

At the moment, only the *software case* is taken into account here. This means: You have created a time_series_data_frame with RESkit or another ETHOS.Suite package, for example. Various meta data can be added here with the *write_time_series_meta_data_software* function. In this particular software case, this is the name of the software and its version. 
Other cases will follow soon. For example, time series from external sources.
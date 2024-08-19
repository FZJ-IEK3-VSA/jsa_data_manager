<a href="https://www.fz-juelich.de/en/ice/ice-2"><img src="https://github.com/FZJ-IEK3-VSA/README_assets/blob/main/JSA-Header.svg?raw=True" alt="Forschungszentrum Juelich Logo" width="300px"></a>
# Jülich System Analysis Data Manager

This library can be used to read and write data and associated metadata according to the Jülich System Analysis metadata Standard.
Currently only the metadata standard for time series data is implemented. Other data types are under discussion.

# Installation of the jsa_data_manager
## 1. Clone jsa_data_manager
```git clone https://jugit.fz-juelich.de/iek-3/shared-code/jsa_data_manager.git```

## 2. Deactivate base environment
permanent solution if you don't want the base env to activate automatically every time 
````conda config --set auto_activate_base false```
or simply
````conda deactivate```
**Important step** else you might run into problems during installation of the package

## 3. Set up an environment
```conda env create -n jsa_data_manager_env --file environment.yml```
or update an existing environment
```conda env update -n jsa_data_manager_env --file environment.yml```

## 4. Activate your environment
```conda activate jsa_data_manager_env```

## 5. Install the papckage
```pip install -e . --no-dependencies```

# Short package description
At the moment you can use this package:
## 1. To read in time series 
An example of how to use jsa_data_manager to read in your time series can be found here: *jsa_data_manager/examples/read_time_series/read_time_series.py*.
Example of the default format for a random timeseries.csv as input: *jsa_data_manager/examples/read_time_series/Random Electricity Time Series.csv*.
See also *jsa_data_manager/examples/write_time_series/Random Electricity Time Series.json* for an example of default metadata structure.
**read_time_series.py** gives you the option of **a.** reading only metadata without times_series.csv, **b.** reading only your meta_data.json or **c.** reading both at the same time. In this case, the names should be the same as well as the storage location of the metadata and time series.

## 2. To write your time series and add the metadata
An example on how to use jsa_data_manager to write your time series + metadata can be found here: *jsa_data_manager/examples/write_time_series*.
**write_time_series.py** gives you the option to 
at the same time, add metadata to your time series and save your time_series_data_frame as a csv and the associated metadata in a destination folder. 

Currently, only the *software case* is taken into account here. This means: You have created a time_series_data_frame with RESkit or another ETHOS.Suite package, for example. Various metadata can be added using the *write_time_series_meta_data_software* function. In this particular software case, this is the name of the software and its version. 
Other cases will follow soon. For example, time series from external sources.

## License

MIT License

Copyright (C) 2024 FZJ-ICE-2

Active Developers: Julian Belina, Lilly Madeisky

You should have received a copy of the MIT License along with this program.
If not, see https://opensource.org/licenses/MIT


## About Us 

<a href="https://www.fz-juelich.de/en/ice/ice-2"><img src="https://github.com/FZJ-IEK3-VSA/README_assets/blob/main/iek3-square.png?raw=True" alt="Institute image ICE-2" width="280" align="right" style="margin:0px 10px"/></a>

We are the <a href="https://www.fz-juelich.de/en/ice/ice-2">Institute of Climate and Energy Systems (ICE) - Jülich Systems Analysis</a> belonging to the <a href="https://www.fz-juelich.de/en">Forschungszentrum Jülich</a>. Our interdisciplinary department's research is focusing on energy-related process and systems analyses. Data searches and system simulations are used to determine energy and mass balances, as well as to evaluate performance, emissions and costs of energy systems. The results are used for performing comparative assessment studies between the various systems. Our current priorities include the development of energy strategies, in accordance with the German Federal Government’s greenhouse gas reduction targets, by designing new infrastructures for sustainable and secure energy supply chains and by conducting cost analysis studies for integrating new technologies into future energy market frameworks.

## Contributions and Support
Every contributions are welcome:
- If you have a question, you can start a [Discussion](https://github.com/FZJ-IEK3-VSA/FINE/discussions). You will get a response as soon as possible.
- If you want to report a bug, please open an [Issue](https://github.com/FZJ-IEK3-VSA/FINE/issues/new). We will then take care of the issue as soon as possible.
- If you want to contribute with additional features or code improvements, open a [Pull request](https://github.com/FZJ-IEK3-VSA/FINE/pulls).


## Acknowledgement

This work was supported by the Helmholtz Association under the program ["Energy System Design"](https://www.helmholtz.de/en/research/research-fields/energy/energy-system-design/).

<p float="left">
<a href="https://www.helmholtz.de/en/"><img src="https://www.helmholtz.de/fileadmin/user_upload/05_aktuelles/Marke_Design/logos/HG_LOGO_S_ENG_RGB.jpg" alt="Helmholtz Logo" width="200px"></a>
</p>
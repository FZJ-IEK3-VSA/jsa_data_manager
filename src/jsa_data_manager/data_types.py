import datetime
import dataclasses
from dataclasses import dataclass
import pandas



@dataclass(slots=True, frozen=True)
class LoadProfileEntry():
    """Represents the energy demand of
    stream or process step in the given time
    period.
    """

    load_type: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    energy_quantity: float
    energy_unit: str
    average_power_consumption: float
    power_unit: str

@dataclass
class LoadProfileMetaData():
    """Provides a list of LoadProfileEntry, a data frame
    from this list and meta data about this list.
    """

    name: str
    object_type: str
    list_of_load_profiles: list[LoadProfileEntry]
    data_frame: pandas.DataFrame
    first_start_time: datetime.datetime
    last_end_time: datetime.datetime
    load_type: str
    power_unit: str
    energy_unit: str
    maximum_energy: float
    maximum_power: float
    minimum_power: float
    total_energy: float
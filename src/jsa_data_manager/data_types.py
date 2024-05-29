import datetime
import dataclasses
from dataclasses import dataclass
import pandas


@dataclass(kw_only=True)
class TimeStampColumnMetaData:
    index_column_number: int
    index_column_name: str
    start_column_number: int
    start_column_name: str
    end_column_number: int
    end_column_name: str


@dataclass(kw_only=True)
class TimeSeriesColumnEntryMetaData:
    column_number: int
    column_name: str
    unit: str
    # optional
    description: str | None = None
    tags: list[str] | None = None
    min: float | None = None
    max: float | None = None
    sum: float | None = None


@dataclass(kw_only=True)
class SoftwareRunData:
    data_source: str
    software_version: str
    user_name: str
    run_guid: str


# software_run_data = SoftwareRunData(
#     data_source="FINE",
#     software_version="2.23.3",
#     user_name="k-schulze",
#     run_guid="1f2e2503-d0db-4736-97f2-c1e504b8dbcb",
# )


@dataclass(kw_only=True)
class TimeSeriesFileMetaData:
    name: str
    data_frame: pandas.DataFrame
    software_run_data: SoftwareRunData
    first_start_time: datetime.datetime
    last_end_time: datetime.datetime
    time_stamp_column_meta_data: TimeStampColumnMetaData
    column_list: list[TimeSeriesColumnEntryMetaData]
    data_format_standard: str


# import subprocess

# res = subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE)
# git_username = res.stdout.strip().decode()
# print(git_username)

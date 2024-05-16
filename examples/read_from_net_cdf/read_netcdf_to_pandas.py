import pathlib
import xarray

current_directory = pathlib.Path(__file__).parent
FILE_NAME = r"test_net_cdf_file.nc4"
path_to_net_cdf = current_directory.joinpath(FILE_NAME)
ds = xarray.open_dataset(path_to_net_cdf)
df = ds.to_dataframe()
print(df)

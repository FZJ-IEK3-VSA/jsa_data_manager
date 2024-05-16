import pathlib
from jsa_data_manager.jsa_data_manager import JSADataManager


current_directory = pathlib.Path(__file__).parent
jsa_data_manager = JSADataManager()

file_name_excel = r"test_load_profile.xlsx"
path_to_excel_file = current_directory.joinpath(file_name_excel)
data_frame = jsa_data_manager.load_profile_data_manager.read_excel_to_data_frame(
    path=path_to_excel_file
)
file_name_csv = r"test_load_profile.csv"
path_to_csv_file = current_directory.joinpath(file_name_csv)
data_frame.to_csv(path_or_buf=path_to_csv_file,sep=",")

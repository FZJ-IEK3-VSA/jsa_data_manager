import pathlib
from jsa_data_manager.jsa_data_manager import JSADataManager


current_directory = pathlib.Path(__file__).parent
jsa_data_manager = JSADataManager()

# file_name_excel = r"test_load_profile.xlsx"
# path_to_excel_file = current_directory.joinpath(file_name_excel)
file_name_csv = r"test_load_profile.csv"
path_to_csv_file = current_directory.joinpath(file_name_csv)

file_name_json = r"test_meta_data.json"
path_to_json_file = current_directory.joinpath(file_name_json)

load_profile_meta_data = (
    jsa_data_manager.load_profile_data_manager.read_load_profile_data(
        path_to_data_frame=path_to_csv_file, path_to_meta_data=path_to_json_file
    )
)

print(load_profile_meta_data)

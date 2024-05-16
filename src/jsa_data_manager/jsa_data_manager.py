import pandas

class DataManagerBase:
    
    def read_csv_to_data_frame(self,path:str)->pandas.DataFrame:
        data_frame=pandas.read_csv(io=path)
        return data_frame
    def read_excel_to_data_frame(self,path:str)->pandas.DataFrame:
        data_frame=pandas.read_excel(io=path)
        return data_frame
    

class LoadProfileDataManager(DataManagerBase):
    def __init__(self) -> None:
        pass

    def read_load_profile_data(self,path_to_data_frame:str,path_to_meta_data:str):
        data_frame=self.


class JSADataManager():
    def __init__(self) -> None:
        self.load_profile_data_manager:LoadProfileDataManager=LoadProfileDataManager()
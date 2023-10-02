from sklearn.datasets import load_breast_cancer
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
import os 
from dataclasses import dataclass

@dataclass
class Data_config:
    path=os.path.join("artifect","data.csv")
class Load_data:
    def __init__(self):
        self.data_path=Data_config()
    def load(self):
        try:
            data = load_breast_cancer()
            x=pd.DataFrame(data.data,columns=data.feature_names)
            x['target']=pd.Series(data.target)
            logging.info(str(x)) 
            x.to_csv(self.data_path.path,index=False)
            logging.info("data saved sucessfully")
        except:
            logging.error('problem in data laod')


# if __init__=="__main__":
l1=Load_data()
l1.load()
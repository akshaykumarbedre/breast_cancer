from sklearn.datasets import load_breast_cancer
from src.logger import logging
from src.exception import CustomException
import pandas as pd 
import os 
from dataclasses import dataclass

from sklearn.datasets import load_breast_cancer
from src.utils import upload_to_mongoDB
class load_dataset():
    def __init__(self):
        pass
    def load_toDatase(self):            
        data_set=load_breast_cancer()
        df=pd.DataFrame(data_set.data,columns=data_set.feature_names)
        df['target']=pd.Series(data_set.target)
        upload_to_mongoDB(df)


data=load_dataset()
data.load_toDatase()

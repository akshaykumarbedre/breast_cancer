from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import os , sys
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import pandas as pd
from src.utils import save_model
@dataclass
class data_transform_config:
    path=os.path.join("artifect","process.pkl")

class Data_transform:
    def __init__(self):
        self.pkl_path=data_transform_config()

    def initial_data_tranform(self,train_path,test_path):
        try:   
           
            train_file=pd.read_csv(train_path)
            test_file=pd.read_csv(test_path)


            train_x=train_file.drop('target',axis=1)
            train_y=train_file['target']
            train_x_proced=self.pipeline_process(train_x)

            train_x_proced['target']=train_y


            test_x=test_file.drop('target',axis=1)
            test_y=test_file['target']
            test_x_proceed=self.pipeline_process(test_x)

            test_x_proceed['target']=test_y
                       
            logging.info(str(train_x_proced.head()))
            logging.info(str(test_x_proceed.head()))
                      
            save_model(self.pl,self.pkl_path.path)
            logging.info('Processsor pickle in created and saved')


            return(
                train_x_proced,test_x_proceed,self.pkl_path.path
            )
        except Exception as e:
            logging.error("error in data Data_transform")
            raise CustomException(e, sys)

    def pipeline_process(self,data):
        self.pl=Pipeline(
                steps=[
                    ("StandardScaler",StandardScaler())
                ,("simpleImputer",SimpleImputer(strategy='mean'))
                ])
        data=pd.DataFrame(self.pl.fit_transform(data),columns=self.pl.get_feature_names_out())
        return data
        


            

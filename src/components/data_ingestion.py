from src.utils import  get_data_From_mongodb
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import os , sys
from sklearn.model_selection import train_test_split

@dataclass
class Data_ingestion_config:
    train_path=os.path.join("artifect","train.csv")
    test_path=os.path.join("artifect","test.csv")

class Data_ingestion:
    def __init__(self):
        self.file_path=Data_ingestion_config()

    def initiate_data_ingestion(self):
        try:
            logging.info("data ingestion start")
            self.data=get_data_From_mongodb()
            train,test= train_test_split(self.data,test_size=0.30,random_state=42)

            train.to_csv(self.file_path.train_path,index=False)
            test.to_csv(self.file_path.test_path,index=False)
            logging.info(str(train.head()))
            logging.info(str(test.head()))
            logging.info("data ingestion complete")

            return (self.file_path.train_path,self.file_path.test_path)
        except Exception as e:
            logging.error(str(e))
            raise CustomException(e, sys) 




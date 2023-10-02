from src.logger import logging
from src.exception import CustomException
import os 
import pandas as pd 
from pymongo import MongoClient
from dataclasses import dataclass
import sys
@dataclass
class Data_config:
    mongodb_path=uri = "mongodb+srv://akshay_kumar:MBhavasar12@cluster0.zdcioit.mongodb.net/?retryWrites=true&w=majority"
def upload_to_mongoDB(df):
    try:
        data=df.to_dict(orient='records')
        logging.info("data loading start")
        uri =Data_config().mongodb_path
        client = MongoClient(uri)
        db=client['DATABASE']
        collection=db['data']
        collection.insert_many(data)
        client.close()

        logging.info("data loading complted")
    except Exception as e:
        print(e)
        logging.error("failed to load data ")
        raise CustomException(e, sys)

def get_data_From_mongodb():
    try:
        url=Data_config().mongodb_path
        client = MongoClient(uri)
        db=client['DATABASE']
        collection=db['data']
        df=pd.DataFrame(list(collection.find()))

        client.close()

        logging.info("data loading  from mongodb complted")
        return df
    except Exception as e:
        print(e)
        logging.error(f"failed to load data {e}")
        raise CustomException(e, sys)

get_data_From_mongodb()
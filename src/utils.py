from src.logger import logging
from src.exception import CustomException
import os 
import pandas as pd 
from pymongo import MongoClient
from dataclasses import dataclass
import pickle
import sys

def upload_to_mongoDB(df):
    try:
        data=df.to_dict(orient='records')
        logging.info("data loading start")
        url="mongodb+srv://akshay_kumar:MBhavasar12@cluster0.zdcioit.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(url)
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
        url="mongodb+srv://akshay_kumar:MBhavasar12@cluster0.zdcioit.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(url)
        db=client['DATABASE']
        collection=db['data']
        df=pd.DataFrame(list(collection.find()))
        df=df.drop("_id",axis=1)
        client.close()
        logging.info("data loading  from mongodb complted")
        return df
    except Exception as e:
        print(e)
        logging.error(f"failed to load data {e}")
        raise CustomException(e, sys)

def save_model(pkl,path):
    try:
        with open(path, 'wb') as file:
            pickle.dump(pkl,file)
            logging.info("saved the pkl file complted ")
    except Exception as e:
        logging.error('error in dump in obj')
        raise CustomException(str(e), sys)

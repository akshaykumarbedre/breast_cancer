from src.components.data_ingestion import Data_ingestion
from src.components.data_transformation import Data_transform
from src.components.model_trainer import Model_trainer

class train_pipeline:
    def __init__(self):
        self.di=Data_ingestion()
        self.dt=Data_transform() 
        self.mt=Model_trainer()


    def train_model(self):
        (train_path,test_path)=self.di.initiate_data_ingestion()
        train_data,test_data,pkl_file=self.dt.initial_data_tranform(train_path,test_path)
        report=self.mt.train_model(train_data,test_data)
        print(report)


tp=train_pipeline()
tp.train_model()
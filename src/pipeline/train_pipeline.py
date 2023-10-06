from src.components.data_ingestion import Data_ingestion
from src.components.data_transformation import Data_transform


di=Data_ingestion()
(train_path,test_path)=di.initiate_data_ingestion()

dt=Data_transform()
train_data,test_data,pkl_file=dt.initial_data_tranform(train_path,test_path)
print(train_data,test_data)


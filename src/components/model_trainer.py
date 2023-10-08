from src.logger import logging
from src.exception import CustomException
import os , pandas as pd 
import sys
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from src.utils import save_model
from dataclasses import dataclass

import warnings
warnings.filterwarnings("ignore")
@dataclass
class model_trainer_config:
    model_path_config=os.path.join("artifect","model.pkl")
class Model_trainer:
    def __init__(self):
        self.model_path=model_trainer_config()
        self.model={
            "SVG":SVC(),
            "RandomForestClassifier":RandomForestClassifier(),
            "KNeighborsClassifier":KNeighborsClassifier(),
            "GaussianNB":GaussianNB()}
    def train_model(self,train_data,test_data):
        try:
            x_train=train_data.iloc[:,:-1]
            x_test=test_data.iloc[:,:-1]
            y_train=train_data.iloc[:,-1:]
            y_test=test_data.iloc[:,-1:]
    
            self.report,self.best_model_name,self.best_model_score=evaluate_model(X_train=x_train,X_test=x_test,y_test=y_test,y_train=y_train,models=self.model)

            self.best_model_object = self.model[self.best_model_name]

            logging.info(f"report : {str(self.report)}  \n best_model:{str(self.best_model_object)}\n bets srocre {str(self.best_model_score)}")

            save_model(self.best_model_object, self.model_path.model_path_config)
            logging.info("model trained sucresfully ")

            return f"report : {str(self.report)}  \n best_model:{str(self.best_model_object)}\n bets srocre {str(self.best_model_score)}"

        except Exception as e:
            logging.error('erroe in maodel trainter')
            raise CustomException(str(e), sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        model_report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)
            # Predict Testing data
            y_test_pred =model.predict(X_test)

            test_model_score = accuracy_score(y_test,y_test_pred)

            model_report[list(models.keys())[i]] =  test_model_score
        
        best_model_score = max(sorted(model_report.values()))

        ## To get best model name from dict

        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]
        return model_report,best_model_name,best_model_score
    
    except Exception as e:
            logging.info('Exception occured during model training')
            raise CustomException(e,sys)

import yaml
from networksecurity.exception.exception import customException
from networksecurity.logging.logger import logging
import os
import sys
import dill
import numpy as np
import pickle
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,"r") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise customException(e,sys)    
    
def write_yaml_file(file_path : str, content:object, replace:bool=False)->None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file:
            yaml.dump(content,file)
    except Exception as e:
        raise customException(e,sys)                
 
def  save_numpy_array(file_path,array:np.array):
    """
    this function is used to store data of a numpy array file
    """
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as fileobj:
            np.save(fileobj,array)
    except Exception as e:
        raise customException(e,sys)    



def save_preprocess_array(file_path:str,obj:object)->None:
    try:
        logging.info("enter the save_obj")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as fileobj:
            pickle.dump(obj,fileobj)
        logging.info("exist the save obj method")  
    except Exception as e:
        customException(e,sys)


def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise customException(f"the file {file_path} does not exist")
        with open(file_path,"rb") as file:
            print(file)
            return pickle.load(file)  
    except Exception as e:
        raise customException(e,sys)

def load_numpy_array_data(file_path:str)->np.array:
    try:
        with open(file_path,"rb") as filr:
            return np.load(file_path)
    except Exception as e:
        raise customException(e,sys)


def evaluate_models(x_train,y_train,x_test,y_test,models,param):
    try:
        report ={}

        for i in range(len(list(models))):
            model=list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs=GridSearchCV(model,para,cv=3)
            gs.fit(x_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)
            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise customException(e,sys)

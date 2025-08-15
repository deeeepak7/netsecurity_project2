import os
import sys
import numpy as np
import pandas as pd


"""
data ingested related constant start with data_ingestion VAR name
"""

Data_ingestion_collection_name: str = "phishingData"
Data_ingestion_database_name: str = "deepakreturn"
Data_ingestion_dir_name:str = "data_ingested"
Data_ingested_feature_store_dir:str = "feature_store"
Data_ingestion_ingested_dir:str = "ingested"
Data_ingested_train_test_spilt_ratio:float = 0.2


"""
defining common constant variable for training pipeline
"""
Target_column = "Result"
Pipeline_name = "networksecurity"
Artifact_dir = "artifact"
File_name = "phishingData.csv"
Train_file_name = "train.csv"
Test_file_name = "test.csv"
Schema_file_path = os.path.join("data_schema","schema.yaml")
saved_model_dir = os.path.join("saved_model")



"""
constant for data validation

"""
Data_Validation_DIR_Name:  str = "data_validation"
Data_Validation_Valid_DIR: str = "validated"
Data_Validation_InValid_DIR: str = "invalid"
Data_Validation_Drift_Report_DIR: str = "drift_report"
Data_Validation_Drift_Report_File_Name:str = "report.yaml"
precossing_object_file_name:str="pickle.pkl"

"""
constant for data validation

"""
data_transformation_dir_name:str="data_transformation"
data_transformation_transformed_data_dir:str="transformed"
data_transformation_transformed_object_dir:str="transformed_object"
##knn inputer used for dealing missing value
data_transformation_imputer_params:dict={
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}

"""
constant of model trainer
"""
model_trainer_dir_name:str="model_trainer"
model_trainer_trained_model_dir:str="trained_model"
model_trainer_trained_model_name:str="model.pkl"
model_trainer_expected_score:float=0.6
model_trainer_over_under_fitting_threshold:float=0.05


"""
constant for model training
"""

model_file_name  = "model.pkl"


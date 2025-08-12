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
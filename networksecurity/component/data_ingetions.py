from networksecurity.exception.exception import customException
from networksecurity.logging.logger import logging

##configuration of data ingested config
from networksecurity.entity.config_entity import dataingestionconfig
from networksecurity.entity.artifact_entity import dataingestionArtifact
import os
import sys
import pymongo
import numpy as np
import pandas as pd
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

mongo_url = os.getenv("mongo_url")
class dataingestion:
    def __init__(self,data_ingestion_config:dataingestionconfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise customException(e,sys)
        
    def export_collection_as_dataframe(self):
        """
        this function export data from mongodb in form of a panda dataframe
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(mongo_url)
            collection = self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop("_id",axis=1,inplace=True)
            df.replace({"na":np.nan},inplace=True) 
            return df   
        except Exception as e:
            raise customException(e,sys)

    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_dir
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise customException(e,sys)

    def  split_data_as_train_test(self,datframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(datframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("performed train test split on the dataframe")
            logging.info("exited split_data_as_train_test method of data_ingestion class")
            dir_path = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info("exporting train test file path")
            train_set.to_csv(self.data_ingestion_config.train_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_file_path,index=False,header=True)
            logging.info("exported train and test file path")
        except Exception as e:
            raise customException(e, sys)

        
    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            datingestionartifact=dataingestionArtifact(train_file_path=self.data_ingestion_config.train_file_path,test_file_path=self.data_ingestion_config.test_file_path)
            return datingestionartifact
        except Exception as e:
            raise customException(e,sys)


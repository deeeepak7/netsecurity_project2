from networksecurity.entity.artifact_entity import dataingestionArtifact
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import customException
from networksecurity.entity.artifact_entity import DataValidationArtifact
from scipy.stats import ks_2samp
import pandas as pd
import numpy as np
import sys
import os
from networksecurity.constant.training_pipeline import Schema_file_path
from networksecurity.util.main_util.utils import read_yaml_file , write_yaml_file

class DataValidation:
    def __init__(self,data_ingestion_artifact:dataingestionArtifact,data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config=read_yaml_file(Schema_file_path)
        except Exception as e:
            raise customException(e,sys)
        


    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise customException(e,sys)  
        



    def validate_number_of_column(self,dataframe:pd.DataFrame)->bool:
        try:
            number_of_column=len(self._schema_config)
            logging.info(f"required no. of column:{number_of_column}")
            logging.info(f"data ftame havs columns:{len(dataframe.columns)}")
            if len(dataframe.columns)==number_of_column:
                return True
            return False
        except Exception as e:
            raise customException(e,sys)

    def detect_dataset_drift(self,base_df,current_df,threshold=0.05)->bool:
        try:
            status=True
            report={}
            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                is_same_distance=ks_2samp(d1,d2)
                if threshold<=is_same_distance.pvalue:
                    is_found=True
                else:
                    is_found=True
                    status=False
                report.update({column:{
                    "p_value":float(is_same_distance.pvalue),
                    "drift_status":is_found
                }})    
            drift_report = self.data_validation_config.drift_report
            dir_path=os.path.dirname(drift_report)
            os.makedirs(dir_path,exist_ok=True) 
            write_yaml_file(file_path=drift_report,content=report) 
        except Exception as e:
            raise customException(e,sys)

    def initiate_dat_validation(self)->DataValidationArtifact:
        try:
            train_file_path=self.data_ingestion_artifact.train_file_path
            test_firl_path=self.data_ingestion_artifact.test_file_path

            ##read data from train and test
            train_dataframe=DataValidation.read_data(train_file_path)
            test_dataframe=DataValidation.read_data(test_firl_path)
            ##valiadte no. of column
            status=self.validate_number_of_column(dataframe=train_dataframe)
            if not status:
                error_message=f"train dataframe doesn't contain all column \n"
            status=self.validate_number_of_column(dataframe=test_dataframe)
            if not status:
                error_message=f"test dataframe doesn't have contain all column \n " 
            ##check for datadrift
            status=self.detect_dataset_drift(base_df=train_dataframe,current_df=test_dataframe)
            dir_path=os.path.dirname(self.data_validation_config.data_train_valid)
            os.makedirs(dir_path,exist_ok=True)
            train_dataframe.to_csv(
                self.data_validation_config.data_train_valid,index=False,header=True
            )
            test_dataframe.to_csv(self.data_validation_config.data_test_valid,index=False,header=True)
            data_validation_artifact=DataValidationArtifact(
                validation_status=status,
                valid_test_file_path=self.data_ingestion_artifact.test_file_path,
                valid_train_file_path=self.data_ingestion_artifact.train_file_path,
                invalid_test_file_path=None,
                invalid_train_file_path=None,
                drift_report=self.data_validation_config.drift_report
            )

            return data_validation_artifact    

        except Exception as e:
            raise customException(e,sys)
        



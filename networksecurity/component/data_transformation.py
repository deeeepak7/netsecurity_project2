import sys
import numpy as np
import os
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from networksecurity.constant.training_pipeline import (Target_column,data_transformation_imputer_params)
from networksecurity.entity.artifact_entity import DataTransformationArtifact,DataValidationArtifact

from networksecurity.exception.exception import customException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.util.main_util.utils import (save_numpy_array,save_preprocess_array)

class Datatranformation:
    def __init__(self,data_validation_artifact:DataValidationArtifact,data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact=data_validation_artifact
            self.data_transformation_config:DataTransformationConfig=data_transformation_config
        except Exception as e:
            raise customException(e,sys)    
    
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise customException(s,sys)
    
    def get_data_transformer_object(cls)->Pipeline:
        """
        it intiatises a knnimputer object with the parameter specified in the traning_pipeline file and return a pipekine obj with a knnimputer obj as first step

        args:
          cls:DataTransformation
        
        return :
          a pipeline object 
        """
        try:
            imputer:KNNImputer =  KNNImputer(**data_transformation_imputer_params)
            logging.info(f"initiate knnimputer with {data_transformation_imputer_params}")
            processor:Pipeline=Pipeline([("imputer",imputer)])
            return processor
        except Exception as e:
            raise customException(e,sys)    


    def initiate_data_transformation(self)->DataTransformationArtifact:
        logging.info("enter initiate_data_transformation method ")
        try:
            logging.info("Starting data transformation")

            train_df=Datatranformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df=Datatranformation.read_data(self.data_validation_artifact.valid_test_file_path)

            ##training dataframe
            input_feature_train_df=train_df.drop(columns=[Target_column],axis=1)
            target_feature_train_df = train_df[Target_column]
            target_feature_train_df=target_feature_train_df.replace(-1,0)

            ##testing dataframe
            input_feature_testing_df= test_df.drop(columns=[Target_column],axis=1)
            target_feature_test_df = test_df[Target_column]
            target_feature_test_df=target_feature_test_df.replace(-1,0)
            
            precossor=self.get_data_transformer_object()

            precossing_object=precossor.fit(input_feature_train_df)
            transformed_input_train_feature=precossing_object.transform(input_feature_train_df)
            transformed_input_test_feature=precossing_object.transform(input_feature_testing_df)

            train_arr=np.c_[transformed_input_train_feature,np.array(target_feature_train_df)]
            test_arr=np.c_[transformed_input_test_feature,np.array(target_feature_test_df)]

            #save numpy array data
            save_numpy_array(self.data_transformation_config.transformed_train_file_path,array=train_arr)
            save_numpy_array(self.data_transformation_config.transformed_test_file_path,array=test_arr)
            save_preprocess_array(self.data_transformation_config.transformed_object_file_path,precossing_object)


            #prepare artifact
            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path = self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path = self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path = self.data_transformation_config.transformed_test_file_path
            )
            return data_transformation_artifact
        except Exception as e:
            raise customException(e,sys)







             






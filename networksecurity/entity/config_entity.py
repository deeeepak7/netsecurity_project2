from datetime import datetime
import os
from networksecurity.constant import training_pipeline

print(training_pipeline.Pipeline_name)


class trainingpipelineconfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.Pipeline_name
        self.artifact_name = training_pipeline.Artifact_dir
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp: str = timestamp


class dataingestionconfig:
    def __init__(self,training_pipeline_config:trainingpipelineconfig):

        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.Data_ingestion_dir_name
        )

        self.feature_store_dir:str=os.path.join(
            self.data_ingestion_dir,
            training_pipeline.Data_ingested_feature_store_dir, training_pipeline.File_name
        )

        self.train_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.Data_ingestion_ingested_dir,training_pipeline.Train_file_name
        )

        self.test_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.Data_ingestion_ingested_dir,training_pipeline.Test_file_name
        )

        self.train_test_split_ratio:float=training_pipeline.Data_ingested_train_test_spilt_ratio
        self.database_name:str=training_pipeline.Data_ingestion_database_name
        self.collection_name:str=training_pipeline.Data_ingestion_collection_name



class DataValidationConfig:

    def __init__(self,training_pipeline_config:trainingpipelineconfig):
        self.data_validation_dir:str=os.path.join(training_pipeline_config.artifact_dir,training_pipeline.Data_Validation_DIR_Name)
        self.data_invalid_dir:str=os.path.join(self.data_validation_dir,training_pipeline.Data_Validation_InValid_DIR)
        self.data_valid_dir:str=os.path.join(self.data_validation_dir,training_pipeline.Data_Validation_Valid_DIR)
        self.data_train_valid:str=os.path.join(self.data_valid_dir,training_pipeline.Train_file_name)
        self.data_test_valid:str=os.path.join(self.data_valid_dir,training_pipeline.Test_file_name)
        self.data_test_invalid:str=os.path.join(self.data_invalid_dir,training_pipeline.Test_file_name)
        self.data_train_invalid:str=os.path.join(self.data_invalid_dir,training_pipeline.Train_file_name)
        self.drift_report:str=os.path.join(self.data_valid_dir,training_pipeline.Data_Validation_Drift_Report_DIR,training_pipeline.Data_Validation_Drift_Report_File_Name)


class DataTransformationConfig:
    def __init__(self,training_pipeline_config:trainingpipelineconfig):
        self.data_transformation_dir:str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.data_transformation_dir_name)  
        self.transformed_train_file_path=os.path.join(self.data_transformation_dir,training_pipeline.data_transformation_dir_name,training_pipeline.Train_file_name.replace("csv","npy"))
        self.transformed_test_file_path=os.path.join(self.data_transformation_dir,training_pipeline.data_transformation_dir_name,training_pipeline.Test_file_name.replace("csv","npy"))
        self.transformed_object_file_path=os.path.join(self.data_transformation_dir,training_pipeline.data_transformation_transformed_object_dir,training_pipeline.precossing_object_file_name)


class ModelTrainingConfig:
    def __init__(self,training_pipeline_config:trainingpipelineconfig):
        self.model_trainer_dir:str=os.path.join(training_pipeline_config.artifact_dir,training_pipeline.model_trainer_dir_name)
        self.trained_model_file_path:str=os.path.join(self.model_trainer_dir,training_pipeline.model_trainer_trained_model_dir,training_pipeline.model_file_name)
        self.excepted_accuracy:float=training_pipeline.model_trainer_expected_score
        self.overfitting_underfitting_threshold=training_pipeline.model_trainer_over_under_fitting_threshold
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
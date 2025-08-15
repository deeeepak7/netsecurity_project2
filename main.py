from networksecurity.component.data_ingetions import dataingestion
from networksecurity.exception.exception import customException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import dataingestionconfig
from networksecurity.entity.config_entity import trainingpipelineconfig
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.component.data_validation import DataValidation,DataValidationConfig
from networksecurity.component.data_transformation import Datatranformation
from networksecurity.entity.config_entity import ModelTrainingConfig
from networksecurity.component.model_trainer import ModelTrainer
if __name__=="__main__":
    try:
        trainpipe=trainingpipelineconfig()
        dataingconfig=dataingestionconfig(trainpipe)
        dataingestion_instance = dataingestion(dataingconfig)
        logging.info("intiate data ingestion")
        dataingestionArtifact = dataingestion_instance.initiate_data_ingestion()
        print(dataingestionArtifact)
        trainpipe = trainingpipelineconfig()
        data_validation_config=DataValidationConfig(trainpipe)
        data_validation=DataValidation(dataingestionArtifact,data_validation_config)
        logging.info("intiate data validation")
        data_validation_artifact=data_validation.initiate_dat_validation()
        logging.info("data validation")
        data_transformation_config=DataTransformationConfig(trainpipe)
        logging.info("data transformation started")
        data_transformation=Datatranformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("transformation completed")
        logging.info("model training artifact")
        model_trainer_config=ModelTrainingConfig(trainpipe)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.inititate_model_trainer()
        logging.info("model training artifact created")
    except Exception as e:
        raise customException(e,sys)
from networksecurity.component.data_ingetions import dataingestion
from networksecurity.exception.exception import customException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import dataingestionconfig
from networksecurity.entity.config_entity import trainingpipelineconfig
if __name__=="__main__":
    try:
        trainpipe=trainingpipelineconfig()
        dataingconfig=dataingestionconfig(trainpipe)
        dataingestion_instance = dataingestion(dataingconfig)
        logging.info("intiate data ingestion")
        dataingestionArtifact = dataingestion_instance.initiate_data_ingestion()
        print(dataingestionArtifact)
    except Exception as e:
        raise customException(e,sys)
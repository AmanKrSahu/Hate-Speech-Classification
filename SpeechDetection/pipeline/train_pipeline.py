import sys
from SpeechDetection.logger import logging
from SpeechDetection.exception import CustomException
from SpeechDetection.components.data_ingestion import DataIngestion
from SpeechDetection.entity.config_entity import (DataIngestionConfig)
from SpeechDetection.entity.artifact_entity import (DataIngestionArtifacts)

class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainingPipeline class")

        try:
            logging.info("Getting the data from GCLoud Storage Bucket")
            
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train and valid from GCloud Storage")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainingPipeline class")

        try:
            data_ingestion_artifacts = self.start_data_ingestion()

            logging.info("Exited the run_pipeline method of TrainingPipeline class")

        except Exception as e:
            raise CustomException(e, sys) from e
        
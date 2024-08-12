from src.TutorialProject.logger import logging
from src.TutorialProject.exception import CustomException
from src.TutorialProject.components.data_ingestion import DataIngestion, DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info('The execution has started')

    try:
        # data_ingestion_config = data_ingestion_config()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
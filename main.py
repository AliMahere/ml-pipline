from mlpipline import logger
from mlpipline.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Main Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
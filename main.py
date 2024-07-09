from mlpipline import logger
from mlpipline.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "val Pipeline"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} complited <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
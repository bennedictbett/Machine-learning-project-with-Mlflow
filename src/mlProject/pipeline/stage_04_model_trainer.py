from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        model_trainer_pipeline = ModelTrainerTrainingPipeline()
        model_trainer_pipeline.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e
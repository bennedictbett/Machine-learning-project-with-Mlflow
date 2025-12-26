import os
from mlProject import logger
from sklearn.model_selection import train_test_split as split_data
import pandas as pd 
from mlProject.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        try:
            logger.info("Reading the data for transformation")
            data = pd.read_csv(self.config.data_path)
            
            logger.info(f"Data shape: {data.shape}")
            logger.info("Splitting the data into train and test sets")
            train_set, test_set = split_data(data, test_size=0.2, random_state=42)  # ✅ Changed here
            
            logger.info(f"Train set shape: {train_set.shape}")
            logger.info(f"Test set shape: {test_set.shape}")
            
            train_file_path = os.path.join(self.config.root_dir, "train.csv")
            test_file_path = os.path.join(self.config.root_dir, "test.csv")
            
            logger.info(f"Saving train set to: {train_file_path}")
            train_set.to_csv(train_file_path, index=False)
            
            logger.info(f"Saving test set to: {test_file_path}")
            test_set.to_csv(test_file_path, index=False)
            
            logger.info("Train and test sets saved successfully")
            logger.info(f"Train size: {len(train_set)}, Test size: {len(test_set)}")
            
            print(f"✅ Train set shape: {train_set.shape}")
            print(f"✅ Test set shape: {test_set.shape}")
            
        except Exception as e:
            logger.error(f"Error during train-test split: {e}")
            raise e
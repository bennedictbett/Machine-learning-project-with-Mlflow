import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from mlProject import logger


class PredictionPipeline:
    def __init__(self):
        """Initialize the prediction pipeline by loading the trained model"""
        try:
            self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
            logger.info("Model loaded successfully for prediction")
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            raise e

    def predict(self, data):
        """
        Make predictions on input data
        
        Args:
            data: pandas DataFrame or numpy array with wine features
            
        Returns:
            numpy array with predictions
        """
        try:
            logger.info(f"Making prediction on data shape: {data.shape}")
            prediction = self.model.predict(data)
            logger.info(f"Prediction completed: {prediction}")
            return prediction
        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            raise e
       
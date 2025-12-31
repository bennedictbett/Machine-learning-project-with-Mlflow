import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
import dagshub
from dotenv import load_dotenv
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_json
from pathlib import Path



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
        # Load environment variables
        load_dotenv()
        
        # Initialize DagsHub
        dagshub.init(repo_owner='bennedictbett', 
                     repo_name='Machine-learning-project-with-Mlflow', 
                     mlflow=True)
        
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        x_test = test_data.drop(columns=[self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        mlflow.set_tracking_uri(self.config.mlflow_url)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(x_test)

            (rmse, mae, r2) = self.eval_metrics(y_test, predicted_qualities)

            # Save metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_path), data=scores)

            # Log parameters to MLflow
            mlflow.log_params(self.config.all_params)

            
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            # Log model
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetWineModel")
            else:
                mlflow.sklearn.log_model(model, "model")
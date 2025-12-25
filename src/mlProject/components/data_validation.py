import os
from mlProject import logger
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            
            # Read the data
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            # Get schema columns
            all_schema = self.config.all_schema.keys()
            
            # Check if all columns match
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    break
            else:
                validation_status = True
            
            # Write validation status to file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            
            return validation_status
        
        except Exception as e:
            raise e
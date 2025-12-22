import os
from box.exceptions import BoxValueError
import yaml
from mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.
    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file '{path_to_yaml}' read successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error converting YAML content to ConfigBox: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading YAML file '{path_to_yaml}': {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose: bool = True):
    """Create directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): Whether to log directory creation.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save a dictionary to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to save.
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load a JSON file and return its contents as a ConfigBox object.

    Args:
        path (Path): Path to the JSON file. 
    Returns:
        ConfigBox: Contents of the JSON file as a ConfigBox object.
    """ 
    with open(path) as f:
        content = json.load(f)
        logger.info(f"JSON file '{path}' loaded successfully.")
        return ConfigBox(content)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save data to a binary file using joblib.

    Args:
        data (Any): Data to save.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")
   
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file.
    Returns:
        Any: Loaded data
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in KB.

    Args:
        path (Path): Path to the file.
    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
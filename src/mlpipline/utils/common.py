import os 
from box.exceptions import BoxValueError
import yaml
from mlpipline import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

@ensure_annotations
def load_json(path: Path) -> dict:
    with open(path, "r") as f:
        logger.info(f"loading json file from {path}")
        return json.load(f)

@ensure_annotations
def save_bin(data: Any, path: Path):
    logger.info(f"Saving file at: {path}")
    joblib.dump(value=data, filename=path)

@ensure_annotations
def load_bin(path: Path) -> Any:
    logger.info(f"Loading file from: {path}")
    return joblib.load(path)
def get_size(path: Path) -> str:
    size_in_mb = round(os.path.getsize(path)/(1024*1024), 2)
    logger.info(f"Size of {path} is {size_in_mb} MB")
    return f"{size_in_mb} MB"

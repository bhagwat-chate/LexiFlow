import os
import sys
import yaml
from exception.custom_exception import DocumentPortalException


def load_config(config_filename: str = "config/config.yaml") -> dict:
    try:
        # Get project root dynamically
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(root_dir, config_filename)

        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
        return config

    except FileNotFoundError as e:
        raise DocumentPortalException(f"Config file not found at {config_path}", sys) from e

    except Exception as e:
        raise DocumentPortalException(e, sys)

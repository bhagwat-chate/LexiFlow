# utils/load_env_secrets.py

import os
import sys
import json
import boto3
from exception.custom_exception import DocumentPortalException


def load_and_set_env_secrets(secret_name="lexiflow_secrets", region="ap-southeast-2"):
    try:
        client = boto3.client('secretsmanager', region_name=region)
        secret_value = client.get_secret_value(SecretId=secret_name)

        secrets = json.loads(secret_value['SecretString'])

        for key, value in secrets.items():
            os.environ[key] = value

        print(f"[Secrets] Loaded {len(secrets)} keys from AWS Secrets Manager")

    except FileNotFoundError as e:
        raise DocumentPortalException(f'secrets not found at secret_name="lexiflow_secrets", region="ap-southeast-2"', sys) from e

    except Exception as e:
        print(f"[Secrets] Failed to load from AWS Secrets Manager: {e}")
        raise

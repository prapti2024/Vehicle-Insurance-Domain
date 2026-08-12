import boto3
import os
from dotenv import load_dotenv
load_dotenv()

from src.constants import (
    AWS_SECRET_ACCESS_KEY_ENV_KEY,
    AWS_ACCESS_KEY_ID_ENV_KEY,
    AWS_ENDPOINT_URL_ENV_KEY,
    REGION_NAME
)


class S3Client:

    s3_client = None
    s3_resource = None

    def __init__(self, region_name=REGION_NAME):
        """
        Creates a connection with S3 using credentials
        and endpoint information from environment variables.
        """

        if S3Client.s3_resource is None or S3Client.s3_client is None:

            access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY)
            secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY)
            endpoint_url = os.getenv(AWS_ENDPOINT_URL_ENV_KEY)

            if access_key_id is None:
                raise Exception(
                    f"Environment variable: {AWS_ACCESS_KEY_ID_ENV_KEY} is not set."
                )

            if secret_access_key is None:
                raise Exception(
                    f"Environment variable: {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set."
                )

            if endpoint_url is None:
                raise Exception(
                    f"Environment variable: {AWS_ENDPOINT_URL_ENV_KEY} is not set."
                )

            S3Client.s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name,
                endpoint_url=endpoint_url
            )

            S3Client.s3_client = boto3.client(
                "s3",
                aws_access_key_id=access_key_id,
                aws_secret_access_key=secret_access_key,
                region_name=region_name,
                endpoint_url=endpoint_url
            )

        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client
import boto3
import botocore
import os
from botocore.exceptions import ClientError
import requests

bucket = os.environ['S3_BUCKET']
object = os.environ['S3_OBJECT']
filename = '/tmp/test.json'

def lambda_handler(event, context):
    data = """{
        "random": "stuff",
        "other": "random stuff"
    }"""

    with open(filename, 'w') as handle:
        handle.write(data)

    upload_file(filename, bucket, object)


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(e)
        return False
    return True
from dotenv import load_dotenv

import boto3
import os


load_dotenv()

BUCKET_NAME = os.getenv('BUCKET_NAME')

session = boto3.session.Session()
s3 = session.client(
    service_name ='s3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id = os.getenv('KEY_ID'),
    aws_secret_access_key = os.getenv('KEY_SECRET')
    )


s3.put_object(Bucket=BUCKET_NAME, Key='newfile', Body='content', StorageClass='STANDARD')

for key in s3.list_objects(Bucket=BUCKET_NAME)['Contents']:
    print(key['Key'])
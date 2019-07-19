
import boto3
import time
from botocore.client import Config

ACCESS_KEY_ID = 'your access id'
ACCESS_SECRET_KEY = 'your secret key'
BUCKET_NAME = 'bucket name'

data = open('download.jpeg', 'rb')

# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
ts = int(time.time())

s3.Bucket(BUCKET_NAME).put_object(Key='Images/'+str(ts)+'.jpeg', Body=data, ACL='public-read')
print(ts)
print ("uploaded Done")


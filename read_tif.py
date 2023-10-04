#!/usr/bin/env python3

import boto3
import botocore

# Initialize the S3 client with anonymous configuration
s3 = boto3.client('s3', region_name='us-west-1', config=boto3.session.Config(signature_version=botocore.UNSIGNED))

# Specify the S3 bucket and prefix
bucket_name = 'globalnightlight'
prefix = 'npp_202309/'

# List the contents of the specified directory
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

data_set = []

# Print the .tif files
for content in response.get('Contents', []):
    if content['Key'].endswith('.tif'):
        data_set.append(content['Key'])


print(data_set, end='\n') # Just printing per line here 

#!/usr/bin/env python3

import boto3
import botocore
import rasterio
import rasterio.env
import matplotlib.pyplot as plt

# Initialize the S3 client with anonymous configuration
s3 = boto3.client('s3', region_name='us-west-1', config=boto3.session.Config(signature_version=botocore.UNSIGNED))

# Specify the S3 bucket and file key
bucket_name = 'globalnightlight'
file_key = 'npp_202309/GDNBO_npp_d20230904_t1528422_e1534226_b61421_c20230904163130543000_oebc_ops.samples.co.tif'


# Create a URL to the .tif file on S3
url = f"s3://{bucket_name}/{file_key}"

# Open the .tif file directly from S3 using rasterio with unsigned request
with rasterio.env.Env(AWS_NO_SIGN_REQUEST='YES'):
    with rasterio.open(url) as src:
        # Read the file into a numpy array
        array = src.read(1)

        # Visualize the array using matplotlib
        plt.imshow(array, cmap='gray')
        plt.colorbar()
        plt.title('Nightlight Data Visualization')
        plt.show()

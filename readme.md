## DynamoDB to S3 Data Transfer

This Python script is designed to copy data from a DynamoDB table to an S3 bucket with a specific structure:
imei/year/month/id.

### Dependencies

This script requires the following dependencies:

boto3 (version 1.17.105 or later)
pyyaml (version 5.4.1 or later)
You can install these dependencies by running the following command in your terminal:

```shell
pip install -r requirements.txt
```

### Configuration

The script reads configuration settings from a config.yaml file. Here is an example config.yaml file:

```yaml

dynamodb:
  region_name: YOUR_DYNAMODB_REGION
  table_name: YOUR_TABLE_NAME
  aws_access_key_id: YOUR_DYNAMODB_ACCESS_KEY_ID
  aws_secret_access_key: YOUR_DYNAMODB_SECRET_ACCESS_KEY
s3:
  region_name: YOUR_S3_REGION
  bucket_name: YOUR_BUCKET_NAME
  aws_access_key_id: YOUR_S3_ACCESS_KEY_ID
  aws_secret_access_key: YOUR_S3_SECRET_ACCESS_KEY
``` 

Make sure to replace YOUR_DYNAMODB_REGION, YOUR_TABLE_NAME, YOUR_S3_REGION, YOUR_BUCKET_NAME,
YOUR_DYNAMODB_ACCESS_KEY_ID, YOUR_DYNAMODB_SECRET_ACCESS_KEY, YOUR_S3_ACCESS_KEY_ID, and YOUR_S3_SECRET_ACCESS_KEY with
the actual values for your DynamoDB table and S3 bucket, as well as your AWS access key ID and secret access key.

### Usage

To use the script, simply run the following command in your terminal:

```python
python3 main.py
```

The script will copy all data from the specified DynamoDB table to the specified S3 bucket with the desired structure.

### License

This script is released under the MIT License.
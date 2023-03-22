import boto3
import time
from datetime import datetime
import yaml


def load_config():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    return config


def copy_data_to_s3():
    config = load_config()
    dynamodb_config = config['dynamodb']
    s3_config = config['s3']
    dynamodb = boto3.resource('dynamodb', region_name=dynamodb_config['region_name'],
                              aws_access_key_id=dynamodb_config.get('aws_access_key_id'),
                              aws_secret_access_key=dynamodb_config.get('aws_secret_access_key'))
    s3 = boto3.resource('s3', region_name=s3_config['region_name'],
                        aws_access_key_id=s3_config.get('aws_access_key_id'),
                        aws_secret_access_key=s3_config.get('aws_secret_access_key'))
    bucket_name = s3_config['bucket_name']
    table_name = dynamodb_config['table_name']
    table = dynamodb.Table(table_name)
    response = table.scan()
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    for item in data:
        imei = item['imei']
        created_at = item['created_at']
        date_time = datetime.fromtimestamp(created_at)
        year = date_time.strftime("%Y")
        month = date_time.strftime("%m")
        id = item['id']
        file_name = f"{imei}/{year}/{month}/{id}"
        s3.Object(bucket_name, file_name).put(Body=str(item))
        print(f"{file_name} has been uploaded to S3")


if __name__ == '__main__':
    copy_data_to_s3()

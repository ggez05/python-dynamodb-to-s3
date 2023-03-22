import boto3
from datetime import datetime
import yaml


def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)


config = load_config()
s3_config = config['s3']
s3 = boto3.resource('s3', region_name=s3_config['region_name'],
                    aws_access_key_id=s3_config.get('aws_access_key_id'),
                    aws_secret_access_key=s3_config.get('aws_secret_access_key'))

bucket_name = s3_config['bucket_name']


def process_items(items):
    for item in items:
        imei = item['imei']
        created_at = item['created_at']
        date_time = datetime.fromtimestamp(created_at)
        year = date_time.strftime("%Y")
        month = date_time.strftime("%m")
        id = item['id']
        file_name = f"{imei}/{year}/{month}/{id}"
        print(file_name)
        s3.Object(bucket_name, file_name).put(Body=str(item))
        print(f"{file_name} has been uploaded to S3")


def copy_data_to_s3():
    print("Start copying data to S3")

    dynamodb_config = config['dynamodb']
    print("Setup dynamodb")
    dynamodb = boto3.resource('dynamodb', region_name=dynamodb_config['region_name'],
                              aws_access_key_id=dynamodb_config.get('aws_access_key_id'),
                              aws_secret_access_key=dynamodb_config.get('aws_secret_access_key'))
    print("Setup dynamodb done")
    table_name = dynamodb_config['table_name']
    table = dynamodb.Table(table_name)
    response = table.scan()
    process_items(response['Items'])
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        process_items(response['Items'])


if __name__ == '__main__':
    copy_data_to_s3()

import json
import urllib.parse
import boto3
import awswrangler as wr



print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    data = wr.s3.read_csv(f"s3://{bucket}/{key}").drop(columns=['Unnamed: 0'])
    prefix = key.split("/")[1].split(".")[0]
    
    print(f"s3://{bucket}/database/{prefix}")
    # Storing data on Data Lake
    wr.s3.to_parquet(
        df=data,
        path=f"s3://{bucket}/database/{prefix}/",
        dataset=True,
        database="streaming_space_database",
        table=prefix
        )
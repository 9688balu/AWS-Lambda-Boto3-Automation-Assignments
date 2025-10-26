import boto3
import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = "dhilipassignment2"
    days = 30
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)

    objects = s3.list_objects_v2(Bucket=bucket)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            if obj['LastModified'] < cutoff:
                s3.delete_object(Bucket=bucket, Key=obj['Key'])
                print(f"Deleted: {obj['Key']}")
            else:
                print(f"Kept: {obj['Key']}")
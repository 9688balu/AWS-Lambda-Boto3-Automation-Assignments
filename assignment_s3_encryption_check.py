import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        name = bucket['Name']
        try:
            s3.get_bucket_encryption(Bucket=name)
            print(f"{name} is encrypted")
        except Exception:
            print(f"{name} has NO encryption")
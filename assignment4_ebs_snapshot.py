import boto3
import datetime

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    volume_id = "vol-0549249a03b634b3f"
    retention_days = 30
    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=retention_days)

    # Create snapshot
    snap = ec2.create_snapshot(VolumeId=volume_id, Description="Automated backup")
    print(f"Created snapshot: {snap['SnapshotId']}")

    # Delete old snapshots
    snapshots = ec2.describe_snapshots(Filters=[{'Name': 'volume-id', 'Values': [volume_id]}])['Snapshots']
    for s in snapshots:
        if s['StartTime'] < cutoff:
            ec2.delete_snapshot(SnapshotId=s['SnapshotId'])
            print(f"Deleted old snapshot: {s['SnapshotId']}")
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Stop Auto-Stop instances
    stop_instances = ec2.describe_instances(Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Stop']}])
    for r in stop_instances['Reservations']:
        for i in r['Instances']:
            state = i['State']['Name']
            if state == 'running':
                ec2.stop_instances(InstanceIds=[i['-068be9db6b91e368e']])
                print(f"Stopped: {i['InstanceId']}")
            else:
                print(f"Skipping {i['InstanceId']} (state={state})")

    # Start Auto-Start instances
    start_instances = ec2.describe_instances(Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Start']}])
    for r in start_instances['Reservations']:
        for i in r['Instances']:
            state = i['State']['Name']
            if state == 'stopped':
                ec2.start_instances(InstanceIds=[i['i-0bcce483b02a09071']])
                print(f"Started: {i['Ii-0bcce483b02a09071']}")
            else:
                print(f"Skipping {i['InstanceId']} (state={state})")
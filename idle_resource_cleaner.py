import boto3
import datetime

# Create AWS service clients
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

# Replace with your actual SNS Topic ARN from your SNS console
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:123456789012:IdleResourcesAlert'

def lambda_handler(event, context):
    report = []
    today = datetime.datetime.utcnow()
    start = today - datetime.timedelta(days=1)

    # Step 1: Get all running EC2 instances
    instances = ec2.describe_instances(Filters=[
        {'Name': 'instance-state-name', 'Values': ['running']}
    ])

    # Step 2: For each instance, check its CPU utilization
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']

            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=start,
                EndTime=today,
                Period=86400,  # 1 day
                Statistics=['Average']
            )

            # If no data, skip
            if not metrics['Datapoints']:
                continue

            avg_cpu = metrics['Datapoints'][0]['Average']

            # Step 3: Identify idle instances (avg CPU < 1%)
            if avg_cpu < 1.0:
                report.append(f"Idle EC2: {instance_id} - {avg_cpu:.2f}% avg CPU")

    # Step 4: Find unattached EBS volumes
    volumes = ec2.describe_volumes(Filters=[
        {'Name': 'status', 'Values': ['available']}
    ])
    for volume in volumes['Volumes']:
        report.append(f"Unattached EBS Volume: {volume['VolumeId']}")

    # Step 5: Send SNS report if idle resources exist
    if report:
        message = "Idle AWS resources detected:\n\n" + "\n".join(report)
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject='AWS Idle Resource Report',
            Message=message
        )

    return {
        'statusCode': 200,
        'body': f"{len(report)} idle resources found."
    }

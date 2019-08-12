import boto3
import datetime
ec2 = boto3.resource('ec2')
client = boto3.client('cloudwatch')
def metric_stat(m,u):
    response= client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName=m,
    Dimensions=[{'Name': "InstanceId", 'Value': 'i-008af2434875a6cc2'}],
    StartTime=datetime.datetime(2019, 2, 4, 19, 0, 0),
    EndTime=datetime.datetime(2019, 2, 4, 23, 0, 0),
    Period=1800,
    Statistics=['Average'],
    Unit=u
    )
    return response

print("Instance ID:".ljust(25)+" i-008af2434875a6cc2")
res = metric_stat('StatusCheckFailed','Count')
first = res['Datapoints']
dp = first[0]
print("Status Check Failed:".ljust(25) + str(dp['Average']))

res = metric_stat('CPUUtilization','Percent')
first = res['Datapoints']
dp = first[0]
print("CPU Utilization:".ljust(25) + str(dp['Average']))

res = metric_stat('NetworkIn','Bytes')
first = res['Datapoints']
dp = first[0]
print("Network In:".ljust(25) + str(dp['Average']))

res = metric_stat('NetworkOut','Bytes')
first = res['Datapoints']
dp = first[0]
print("Network Out:".ljust(25) + str(dp['Average']))
import boto3
import datetime
import smtplib
ec2 = boto3.resource('ec2')
client = boto3.client('cloudwatch')
fromaddr = "sahanacuboulder@gmail.com"
toaddrs = 'sasa7902@colorado.edu'

def metric_stat(i,m,u):
    response= client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName=m,
    Dimensions=[{'Name': "InstanceId", 'Value': i}],
    StartTime=datetime.datetime.now()- datetime.timedelta(days=1),
    EndTime=datetime.datetime.now()+ datetime.timedelta(days=1),
    Period=1800,
    Statistics=['Average'],
    Unit=u
    )
    return response

def stop_instance(i):
    ids_to_be_stopped = []
    ids_to_be_stopped.append(i)
    ec2.instances.filter(InstanceIds=ids_to_be_stopped).stop()

def send_mail(i1,i2,Threshold):
    username = "sahanacuboulder@gmail.com"
    password = "bengaluru123"
    msg = "Shut down the Instance " +i1+ "as its CPU utilization crossed a Threshold of" +str(Threshold)+"% \n and Spinned up the instance "+i2
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    print(msg+"-----> sent to"+toaddrs)
    
ids=['i-03bb7779c4e5611f1','i-03bb7779c4e5611f1']

Threshold = 0.05
while True:
    res = metric_stat(ids[0],'CPUUtilization','Percent')
    first = res['Datapoints']
    dp = first[0]
    value =float(dp['Average'])
    if value > Threshold:
        stop_instance(ids[0])
        instance = ec2.create_instances(ImageId='ami-0ad16744583f21877', MinCount=1, MaxCount=1,InstanceType='t2.micro')
        send_mail(ids[0], instance[0].id, Threshold)
        break
    res = metric_stat(ids[1],'CPUUtilization','Percent')
    first = res['Datapoints']
    dp = first[0]
    value =float(dp['Average'])
    if value > Threshold:
        stop_instance(ids[1])
        instance = ec2.create_instances(ImageId='ami-0ad16744583f21877', MinCount=1, MaxCount=1,InstanceType='t2.micro')
        send_mail(ids[1], instance[0].id, Threshold)
        break

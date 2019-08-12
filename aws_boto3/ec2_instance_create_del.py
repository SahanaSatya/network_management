import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(ImageId='ami-0ad16744583f21877', MinCount=1, MaxCount=2,InstanceType='t2.micro')
for instance in instances:
    print("Created Instance:",instance.id, instance.instance_type)

running_instances_id = []    
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    running_instances_id.append(instance.id)
    
ids_to_be_stopped = []
ids_to_be_stopped.append(running_instances_id[1])

ec2.instances.filter(InstanceIds=ids_to_be_stopped).stop()
print("Stopped instances",ids_to_be_stopped)

print("[Instance Id]".ljust(20)+"[Instance_type]".ljust(20)+"[Instance_ip_address]".ljust(25)+"Running/Stopped".ljust(20))
instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
    print(str(instance.id).ljust(20)+str(instance.instance_type).ljust(20)+str(instance.private_ip_address).ljust(25)+"Running")

instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
for instance in instances:
    print(str(instance.id).ljust(20)+str(instance.instance_type).ljust(20)+str(instance.private_ip_address).ljust(25)+"stopped")

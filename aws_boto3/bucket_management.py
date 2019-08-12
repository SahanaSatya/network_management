import boto3
import datetime
import re
import time
s3r = boto3.resource('s3')
s3 = boto3.client('s3')
s3r.create_bucket(Bucket='netman-sahana', CreateBucketConfiguration={'LocationConstraint': 'us-west-1'})

timestamp = str(datetime.datetime.now())
s3.upload_file("abc.txt", 'netman-sahana', "abc_"+timestamp+".txt")
s3.upload_file("qwerty.jpg", 'netman-sahana', "qwerty_"+timestamp+".jpg")

print("The contents of the bucket are:")
for k in s3.list_objects(Bucket='netman-sahana')['Contents']:
    print(k['Key'])

b1 = s3r.Bucket('netman-sahana')
obj1 = b1.objects.all()

print("Going to sleep for 360 seconds in order to demonstrate the removal of aged files")
time.sleep( 360 )
timestamp = str(datetime.datetime.now())
m = re.findall(r'\d+',timestamp)
min = int(m[4])
for obj in obj1:
    t = re.findall(r'\d+',str(obj.last_modified))
    time1 = int(t[4])
    if (min - time1) >=5:
        print("Deleting the file "+str(obj.key)+"as it is older than 5 minutes")
        s3r.Object('netman-sahana', obj.key).delete() 
    
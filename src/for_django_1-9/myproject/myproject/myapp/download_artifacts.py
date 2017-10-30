import boto3
from subprocess import Popen, PIPE
import json
import pexpect
from pexpect import pxssh
import subprocess
import time

client = boto3.client('devicefarm')
project_arn='arn:aws:devicefarm:us-west-2:872679983532:project:50432bec-470f-4f08-8fe4-b30d180aec76'
device_pool_arn='arn:aws:devicefarm:us-west-2:872679983532:devicepool:50432bec-470f-4f08-8fe4-b30d180aec76/25bee606-275d-48b7-aad2-74d73ec6b99b'
create_upload_command='aws devicefarm create-upload --project-arn "arn:aws:devicefarm:us-west-2:872679983532:project:50432bec-470f-4f08-8fe4-b30d180aec76" --name BitbarIOSSample.ipa --type IOS_APP'
schedule_upload_command=''
file_location='BitbarIOSSample.ipa'
list_devices =['Apple iPad 5th Generation', 'Apple iPad Pro 9.7','Apple iPhone 7']


response_list_jobs=client.list_jobs(
    arn='arn:aws:devicefarm:us-west-2:872679983532:run:50432bec-470f-4f08-8fe4-b30d180aec76/17cb4ac4-2ce3-488d-8b1e-8f77d93ffad2'
)

job_aritifact_arn={}

for i in range(0,3):
    key= response_list_jobs['jobs'][i]['name']
    response_job = client.list_artifacts(
        arn=response_list_jobs['jobs'][i]['arn'],
        type='FILE'
    )
    val= response_job['artifacts'][5]['url']
    job_aritifact_arn[key]=val

print job_aritifact_arn





#print "The job artifacts are "

#print response_job['artifacts'][5]['type']
#print response_job['artifacts'][5]['type']


# r = json.dumps(response)
# loaded_r = json.loads(r)
# print loaded_r

#dict= response['artifacts'][5]
#print dict['type']
# counter=0;
# while(True):
#      dict= response['artifacts'][counter]
#      if dict['type']=='VIDEO':
#          print dict['url']
#      counter=counter+1

#print ['url']

# while(True):
#     counter=0;
#     dict= response['artifacts'][counter]
#     if dict['type']=='VIDEO':
#         print dict['url']
#     counter=counter+1


#print response['artifacts'][0]
#print response

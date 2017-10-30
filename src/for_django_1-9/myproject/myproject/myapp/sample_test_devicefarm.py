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

print client

response = client.list_device_pools(arn='arn:aws:devicefarm:us-west-2:872679983532:project:50432bec-470f-4f08-8fe4-b30d180aec76')
response1 = client.list_device_pools(arn='arn:aws:devicefarm:us-west-2:872679983532:project:50432bec-470f-4f08-8fe4-b30d180aec76')


def command_create_upload(filename,project_arn,app_type):

    # response = client.create_upload(
    #     projectArn=project_arn,
    #     name=filename,
    #     type=app_type,
    #     contentType='string'
    # )
    # url=response['upload']['url']
    # app_urn=response['upload']['arn']
    #
    # print url
    # print app_urn

    # response_get_upload = client.get_upload(
    #     arn=app_urn
    # )
    # status=response_get_upload['upload']['status']
    # print status
    command_to_upload = subprocess.Popen('aws devicefarm create-upload --project-arn "' + project_arn + '" --name BitbarIOSSample.ipa --type IOS_APP',stdout=subprocess.PIPE, shell=True)
    # (output, err) = ip_addr.communicate()
    (output, err) = command_to_upload.communicate()
    print "GOing to print AWS Device Farm Create upload request"
    print output

    d = json.loads(output)
    url= d['upload']['url']
    app_arn= d['upload']['arn']

    command_to_upload_via_curl="curl -T "+file_location+" "+'"'+url+'"'
    print command_to_upload_via_curl
    upload_output = subprocess.Popen(command_to_upload_via_curl, stdout=subprocess.PIPE, shell=True)
    (curl_output, err) = upload_output.communicate()
    print curl_output


    time.sleep(5)


    print "Going to get the status of APP UPLOAD"

    response_get_upload = client.get_upload(arn=app_arn)
    status=response_get_upload['upload']['status']
    print status
    if status=='SUCCEEDED':
        response_schedule_run = client.schedule_run(
            projectArn=project_arn,
            appArn=app_arn,
            devicePoolArn=device_pool_arn,
            name='First_Test_Program',
            test={
                'type': 'BUILTIN_FUZZ'})
        print response_schedule_run['run']['status']
    get_run_arn=response_schedule_run['run']['arn']
    print "The value of run arn is  "+get_run_arn

    while(True):
        response_get_run = client.get_run(arn=get_run_arn)
        status_run=response_get_run['run']['status']
        print status_run
        #arn_run=run=response_get_run['run']['arn']
        #print arn_run
        if status_run=='COMPLETED':
            break
        else:
            time.sleep(200)
            print "The tests are running. Please wait"

    print "The Tests ran Successfully"






    #status = response_get_upload['upload']['status']
    #print status


def upload_to_aws_device_farm(project_arn, app_arn, device_pool_arn,test_name, test_type):
    command_create_upload("BitbarIOSSample.ipa",project_arn,'IOS_APP')





command_create_upload("BitbarIOSSample.ipa",project_arn,'IOS_APP')





#
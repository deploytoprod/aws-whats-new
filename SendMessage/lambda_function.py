import json
import boto3
from botocore.vendored import requests
from boto3.dynamodb.types import TypeDeserializer
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import botocore.exceptions
import os
from time import sleep
import base64
import hmac
import hashlib

def postToChime(msg):

  headers = {
    'Content-Type': 'application/json',
  }

  data = "{\"Content\":\""+msg+"\"}"
  try:
    ssm = boto3.client('ssm')
    ssmparam = ssm.get_parameters(
      Names=[os.environ['PARAMETER_NAME']],
      WithDecryption=True
    )
  except ClientError as error:
    print('Problem getting keys from SSM: {}'.format(error))
    return {
        'statusCode': 501,
        'body': 'Problem getting parameter'
    }
  paramvalue = ssmparam['Parameters'][0]['Value']
  response = requests.post(paramvalue, headers=headers, data=data)


def lambda_handler(event, context):

  for record in event['Records']:
    try:
      link = record['dynamodb']['NewImage']['link']['S']
      title = record['dynamodb']['NewImage']['title']['S']
      published = record['dynamodb']['NewImage']['published']['S']
      msg = "/md [" + title + "](" + link + ") - published at " + published
      print(msg)
      postToChime(msg)
      sleep(1)
    except:
      pass

  return {
    'statusCode': 200,
    'body': json.dumps('Hello from Lambda!')
  }

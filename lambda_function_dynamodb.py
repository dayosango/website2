# Updates pushed from GitHub repository
import json, csv, boto3, urllib
from datetime import datetime

s3 = boto3.resource('s3')
s3bucket = "finalproject-ds-oc"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('readers_details')

def lambda_handler(event, context):
   # Save information to DynamoDB table
   dt = datetime.now().strftime("%Y%m%d%H%M%S")
   filename = dt + "readers_details_info.json"
   s3_path = "data/" + filename
   objectpath = "https://" + s3bucket + ".s3.amazonaws.com/" + s3_path
   item = "{'Entry': {" + dt + "},'link': { " + s3_path + "}"
   table.put_item(Item={'id': 2 ,
   'Age': 35,
   'Comment' : 'So interesting',
   'First Name' : 'Sarah',
   'Last Name' : 'Smith',
   'Phone' : '7654987882',
   'Postcode' : 'E8 3RF' })
   
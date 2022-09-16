import boto3
import logging
def lambda_handler(event, context):
 client = boto3.client(‘sagemaker’)
 client.start_notebook_instance(NotebookInstanceName=’Modelos’)
 return 0
 
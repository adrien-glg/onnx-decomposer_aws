import boto3
import utils

sfn_client = boto3.client('stepfunctions')

execution_arn = utils.get_execution_arn()

response = sfn_client.describe_execution(
    executionArn=execution_arn
)

print(response['output'])

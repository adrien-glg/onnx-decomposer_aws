import boto3
import utils
import sfn_constants

sfn_client = boto3.client('stepfunctions')

execution_arn = utils.get_execution_arn()

response = sfn_client.describe_execution(
    executionArn=execution_arn
)

utils.save_to_file(response, sfn_constants.EXECUTION_DESCRIPTION)

print(response)

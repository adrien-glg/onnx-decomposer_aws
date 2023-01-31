import boto3
import json
import utils
import sfn_constants

sfn_client = boto3.client('stepfunctions')

state_machine_arn = utils.get_state_machine_arn()

print("Please wait while execution is running...")

response = sfn_client.start_sync_execution(
    stateMachineArn=state_machine_arn,
    input=json.dumps({})
)

utils.save_to_file(response['executionArn'], sfn_constants.EXECUTION_ARN_FILE)

print(response['output'])
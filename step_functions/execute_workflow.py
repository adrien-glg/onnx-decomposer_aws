import boto3
import json
import utils
import sfn_constants

sfn_client = boto3.client('stepfunctions')

state_machine_arn = utils.get_state_machine_arn()

response = sfn_client.start_execution(
    stateMachineArn=state_machine_arn,
    input=json.dumps({})
)

utils.save_to_file(response, sfn_constants.EXECUTION_OUTPUT)

print(response)
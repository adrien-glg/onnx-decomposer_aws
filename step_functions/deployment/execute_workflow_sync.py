import boto3
import json
import pprint

from step_functions.deployment import sfn_constants
from step_functions.deployment import utils


sfn_client = boto3.client('stepfunctions')

state_machine_arn = utils.get_state_machine_arn()

print("STATE MACHINE ARN: " + state_machine_arn)
print("\nPlease wait while the execution is running...\n")

response = sfn_client.start_sync_execution(
    stateMachineArn=state_machine_arn,
    input=json.dumps({})
)

utils.save_to_file(response['executionArn'], sfn_constants.EXECUTION_ARN_FILE)

if response['status'] == 'FAILED':
    pprint.pprint(response)
    print("\nThe execution has failed")
elif response['status'] == 'SUCCEEDED':
    pprint.pprint(response['output'])
    print("\nThe execution has succeeded")
else:
    pprint.pprint(response)

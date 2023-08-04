import boto3
import json
import pprint

from step_functions.deployment import sfn_constants
from step_functions.deployment import utils


sfn_client = boto3.client('stepfunctions')

state_machine_arn = utils.get_state_machine_arn()

print("STATE MACHINE ARN: " + state_machine_arn)
print("\nStarting inference...")
print("Please wait while the execution is running...")

response = sfn_client.start_sync_execution(
    stateMachineArn=state_machine_arn,
    input=json.dumps({})
)

utils.save_to_file(response['executionArn'], sfn_constants.EXECUTION_ARN_FILE)

if response['status'] == 'FAILED':
    pprint.pprint(response)
    print("Inference failed")
elif response['status'] == 'SUCCEEDED':
    # pprint.pprint(response['output'])
    output = response['output']
    output_json = json.loads(output)
    print("Inference successful")
    print("\nRESULTS:")
    print(output_json["result"])
else:
    pprint.pprint(response)

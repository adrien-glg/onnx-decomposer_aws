import pprint
import sys

import boto3
import json
import utils
import sfn_constants

if len(sys.argv) == 1:
    concurrent_executions = 1
else:
    concurrent_executions = int(sys.argv[1])

sfn_client = boto3.client('stepfunctions')

state_machine_arn = utils.get_state_machine_arn()
print("STATE MACHINE ARN: " + state_machine_arn + "\n")

for i in range(concurrent_executions):
    response = sfn_client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps({})
    )
    print("Execution " + str(i) + " has started")

# pprint.pprint(response)

utils.save_to_file(response['executionArn'], sfn_constants.EXECUTION_ARN_FILE)


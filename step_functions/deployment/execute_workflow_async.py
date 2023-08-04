import sys
import boto3
import json
import time

from step_functions.deployment import sfn_constants
from step_functions.deployment import utils


if len(sys.argv) == 1:
    concurrent_executions = 1
else:
    number_of_batches = len(sys.argv) - 1
    for i in range(1, len(sys.argv)):
        concurrent_executions = [int(n) for n in sys.argv[1:]]

sfn_client = boto3.client('stepfunctions')

state_machine_arn = utils.get_state_machine_arn()
print("STATE MACHINE ARN: " + state_machine_arn + "\n")

for i in range(len(concurrent_executions)):
    for j in range(concurrent_executions[i]):
        response = sfn_client.start_execution(
            stateMachineArn=state_machine_arn,
            input=json.dumps({})
        )
        print("Started execution " + str(i*concurrent_executions[i] + j + 1).zfill(2))
    if i + 1 < len(concurrent_executions):
        print("\nWaiting 30 seconds...\n")
        time.sleep(30)

utils.save_to_file(response['executionArn'], sfn_constants.EXECUTION_ARN_FILE)

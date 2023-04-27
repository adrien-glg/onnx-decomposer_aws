import boto3
import pprint

from step_functions.deployment import utils


sfn_client = boto3.client('stepfunctions')

state_machine_arn = utils.get_state_machine_arn()

response = sfn_client.describe_state_machine(
    stateMachineArn=state_machine_arn
)

pprint.pprint(response)

import boto3
from datetime import datetime, timedelta
import pprint

from step_functions.deployment import sfn_constants
from step_functions.deployment import utils

logs_client = boto3.client('logs')

print(sfn_constants.FUNCTION_NAME + "\n")


response = logs_client.filter_log_events(
    # logGroupName='/aws/lambda/' + sfn_constants.FUNCTION_NAME,
    # logStreamNamePrefix="2023/03/07",
    # filterPattern='REPORT',
)

events = response['events']

pprint.pprint(response)
import boto3
from datetime import datetime, timedelta
import pprint

import sfn_constants
import utils

logs_client = boto3.client('logs')

def get_logs():
    yesterday = datetime.now() - timedelta(days=1)

    response = logs_client.filter_log_events(
        logGroupName='/aws/lambda/' + sfn_constants.FUNCTION_NAME,
        logStreamNamePrefix=utils.get_today_date(),
        filterPattern='REPORT',
    )

    events = response['events']

    for i in range(len(events)):
        print("\n---------------------------------\n")

        message = events[i]['message']

        pprint.pprint(message)

        print("\nDURATION:")
        print((utils.get_duration(message)))

        print("\nBILLED DURATION:")
        print((utils.get_duration(message, billed=True)))

        print("\nMAX MEMORY USED:")
        print((utils.get_memory_used(message)))

get_logs()
import boto3
from datetime import datetime, timedelta
import pprint

import sfn_constants
import utils

logs_client = boto3.client('logs')

def get_metrics():
    yesterday = datetime.now() - timedelta(days=1)

    response = logs_client.filter_log_events(
        logGroupName='/aws/lambda/' + sfn_constants.FUNCTION_NAME,
        #logStreamNamePrefix=utils.get_today_date(),
        # DO NOT FORGET TO FIX THIS, WHAT DATE SHOULD I KEEP ETC?? START TIME? END TIME?
        logStreamNamePrefix="2023/02/25",
        filterPattern='REPORT',
    )

    metrics_list, metrics_list_with_units = [], []
    events = response['events']

    for i in range(len(events)):
        message = events[i]['message']
        #execution_number = len(events) - (i + 1)
        execution_number = i
        duration = utils.get_duration(message)
        billed_duration = utils.get_duration(message, billed=True)
        used_memory = utils.get_used_memory(message)
        metrics = [sfn_constants.FUNCTION_NAME, execution_number, duration[0], billed_duration[0], used_memory[0]]
        metrics_with_units = [sfn_constants.FUNCTION_NAME, execution_number, duration, billed_duration, used_memory]
        metrics_list += [metrics]
        metrics_list_with_units += [metrics_with_units]

    #metrics_list.reverse()
    #metrics_list_with_units.reverse()

    return metrics_list, metrics_list_with_units


def print_metrics(metrics_list):
    print("LAMBDA FUNCTION: " + sfn_constants.FUNCTION_NAME + "\n")
    for i in range(len(metrics_list)):
        print("EXECUTION NUMBER: " + str(metrics_list[i][1]))
        print("DURATION: " + str(metrics_list[i][2]))
        print("BILLED DURATION: " + str(metrics_list[i][3]))
        print("MAX MEMORY USED: " + str(metrics_list[i][4]))
        if (i + 1) < len(metrics_list):
            print("-----------------------------------")


metrics, metrics_with_unit = get_metrics()
print_metrics(metrics_with_unit)

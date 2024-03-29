import boto3

from step_functions.deployment import sfn_constants
from step_functions.deployment import utils


def get_metrics():
    logs_client = boto3.client('logs')
    response = logs_client.filter_log_events(
        logGroupName='/aws/lambda/' + sfn_constants.FUNCTION_NAME,
        logStreamNamePrefix=utils.get_today_date(),
        filterPattern='REPORT',
    )

    metrics_list, metrics_list_with_units = [], []
    events = response['events']

    for i in range(len(events)):
        message = events[i]['message']
        timestamp = events[i]['timestamp']
        # timestamp = events[i]['timestamp'] // 100
        # timestamp = int(str(timestamp)[5:])
        duration = utils.get_duration(message)
        used_memory = utils.get_used_memory(message)
        metrics = [timestamp, duration[0], used_memory[0]]
        metrics_with_units = [timestamp, duration, used_memory]
        metrics_list += [metrics]
        metrics_list_with_units += [metrics_with_units]

    return metrics_list, metrics_list_with_units


def print_metrics(metrics_list):
    print("LAMBDA FUNCTION: " + sfn_constants.FUNCTION_NAME + "\n")
    if len(metrics_list) == 0:
        print("NO METRICS TO DISPLAY")
        print("\nPlease wait around 30 seconds after all the executions have completed")
    else:
        for i in range(len(metrics_list)):
            print("TIMESTAMP:        " + str(metrics_list[i][0]))
            print("DURATION:         " + str(metrics_list[i][1][0]) + " " + str(metrics_list[i][1][1]))
            print("MAX MEMORY USED:  " + str(metrics_list[i][2][0]) + " " + str(metrics_list[i][2][1]))
            if (i + 1) < len(metrics_list):
                print("-----------------------------------")


if __name__ == '__main__':
    metrics, metrics_with_unit = get_metrics()
    print_metrics(metrics_with_unit)

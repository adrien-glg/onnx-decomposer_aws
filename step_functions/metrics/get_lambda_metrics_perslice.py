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

    log_streams = []
    durations, durations_with_units = [], []
    memories, memories_with_units = [], []

    events = response['events']

    for i in range(len(events)):
        message = events[i]['message']
        duration = utils.get_duration(message)
        memory = utils.get_used_memory(message)
        log_stream = events[i]['logStreamName']
        if log_stream not in log_streams:
            log_streams += [log_stream]
            durations += [[duration[0]]]
            durations_with_units += [[duration]]
            memories += [[memory[0]]]
            memories_with_units += [[memory]]
        else:
            index = log_streams.index(log_stream)
            durations[index] += [duration[0]]
            durations_with_units[index] += [duration]
            memories[index] += [memory[0]]
            memories_with_units[index] += [memory]

    return durations, durations_with_units, memories, memories_with_units


def print_metrics(durations_list, memories_list):
    print("LAMBDA FUNCTION: " + sfn_constants.FUNCTION_NAME)
    if len(durations_list) == 0:
        print("\nNO METRICS TO DISPLAY")
        print("\nPlease wait around 30 seconds after all the executions have completed")
    else:
        for i in range(len(durations_list)):
            print("\n-----------------------------------")
            print("-----------------------------------")
            print("EXECUTION:        " + str(i + 1))
            print("-----------------------------------")
            for j in range(len(durations_list[i])):
                print("-----------------------------------")
                print("SLICE:            " + str(j + 1))
                print("DURATION:         " + str(durations_list[i][j][0]) + " " + str(durations_list[i][j][1]))
                print("MAX MEMORY USED:  " + str(memories_list[i][j][0]) + " " + str(memories_list[i][j][1]))


if __name__ == '__main__':
    durations, durations_with_units, memories, memories_with_units = get_metrics()
    print_metrics(durations_with_units, memories_with_units)

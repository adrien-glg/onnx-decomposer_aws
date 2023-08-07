import csv
import os
import sys

from step_functions.metrics import get_lambda_metrics_executions, get_lambda_metrics_perslice,\
    get_lambda_metrics_timestamps
from step_functions.deployment import sfn_constants


def write_metrics(metrics_file, file_headers, obtained_metrics):
    if not os.path.exists(sfn_constants.METRICS_FOLDER):
        os.mkdir(sfn_constants.METRICS_FOLDER)

    with open(metrics_file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(file_headers)
        writer.writerows(obtained_metrics)


def write_metrics_perslice(duration_list, memory_list):
    with open(sfn_constants.METRICS_FILE_PERSLICE, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(sfn_constants.CSV_HEADERS_PERSLICE)
        for i in range(len(duration_list)):
            for j in range(len(duration_list[i])):
                writer.writerow([i + 1, j + 1, duration_list[i][j], memory_list[i][j]])


if __name__ == '__main__':
    error_message = "Please enter a correct mode as argument: executions, timestamps, perslice"
    if len(sys.argv) != 2:
        raise Exception(error_message)
    else:
        mode = sys.argv[1]
        print("MODE: " + mode + "\n")
        print("Saving metrics to CSV file...")
        if mode == "executions":
            file = sfn_constants.METRICS_FILE
            metrics = get_lambda_metrics_executions.get_metrics()[0]
            write_metrics(file, sfn_constants.CSV_HEADERS_EXECUTIONS, metrics)
        elif mode == "timestamps":
            file = sfn_constants.METRICS_FILE_TIMESTAMPS
            metrics = get_lambda_metrics_timestamps.get_metrics()[0]
            write_metrics(file, sfn_constants.CSV_HEADERS_TIMESTAMPS, metrics)
        elif mode == "perslice":
            file = sfn_constants.METRICS_FILE_PERSLICE
            metrics = get_lambda_metrics_perslice.get_metrics()
            durations, memories = metrics[0], metrics[2]
            write_metrics_perslice(durations, memories)
        else:
            raise Exception(error_message)
        print("Saved metrics successfully to " + file)


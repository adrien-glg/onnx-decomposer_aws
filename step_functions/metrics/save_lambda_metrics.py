import csv
import os

from step_functions.metrics import get_lambda_metrics
from step_functions.deployment import sfn_constants

durations, durations_with_units, memories, memories_with_units = get_lambda_metrics.get_metrics()
# total_exec_time = get_workflow_metrics.get_total_exec_times()[0]

if durations:
    if not os.path.exists(sfn_constants.METRICS_FOLDER):
        os.mkdir(sfn_constants.METRICS_FOLDER)

    with open(sfn_constants.METRICS_FILE, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(sfn_constants.CSV_HEADERS)
        for i in range(len(durations)):
            for j in range(len(durations[i])):
                writer.writerow([i, j, durations[i][j], memories[i][j]])

    # write_headers = not os.path.exists(sfn_constants.TOTAL_TIME_FILEPATH)
    # with open(sfn_constants.TOTAL_TIME_FILEPATH, 'a', encoding='UTF8', newline='') as f:
    #     writer = csv.writer(f)
    #     if write_headers:
    #         writer.writerow(sfn_constants.TOTAL_TIME_HEADERS)
    #     writer.writerow([sfn_constants.FUNCTION_NAME, total_exec_time])




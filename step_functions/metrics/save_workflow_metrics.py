import csv
import os

from step_functions.metrics import get_workflow_metrics
from step_functions.deployment import sfn_constants


total_exec_time = get_workflow_metrics.get_total_exec_times()[0]

write_headers = not os.path.exists(sfn_constants.TOTAL_TIME_FILEPATH)
with open(sfn_constants.TOTAL_TIME_FILEPATH, 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    if write_headers:
        writer.writerow(sfn_constants.TOTAL_TIME_HEADERS)
    writer.writerow([sfn_constants.FUNCTION_NAME, total_exec_time])

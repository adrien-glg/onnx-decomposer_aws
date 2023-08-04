import csv
import os

from step_functions.metrics import get_lambda_metrics_timestamps
from step_functions.deployment import sfn_constants

metrics = get_lambda_metrics_timestamps.get_metrics()[0]
headers = sfn_constants.CSV_HEADERS_TIMESTAMPS

if not os.path.exists(sfn_constants.METRICS_FOLDER):
    os.mkdir(sfn_constants.METRICS_FOLDER)

with open(sfn_constants.METRICS_FILE_TIMESTAMPS, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(metrics)

import csv
import os

from step_functions.metrics import get_lambda_metrics
from step_functions.deployment import sfn_constants

metrics = get_lambda_metrics.get_metrics()[0]

if not os.path.exists(sfn_constants.METRICS_FOLDER):
    os.mkdir(sfn_constants.METRICS_FOLDER)

with open(sfn_constants.METRICS_FILE, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(sfn_constants.CSV_HEADERS)
    writer.writerows(metrics)
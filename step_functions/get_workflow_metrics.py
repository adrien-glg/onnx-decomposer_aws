import boto3
from datetime import datetime, timedelta
import pprint


cloudwatch_client = boto3.client('cloudwatch')
# cloudwatch = boto3.resource('cloudwatch')
# metric = cloudwatch.Metric('namespace','name')

# response = cloudwatch_client.list_metrics()

yesterday = datetime.now() - timedelta(days=1)

response = cloudwatch_client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'a5869708',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/States',
                    'MetricName': 'ExpressExecutionMemory',
                },
                'Period': 3600,
                'Stat': 'TM(0%:100%)',
            },
        },
    ],
    StartTime=yesterday,
    EndTime=datetime.now(),
)

pprint.pprint(response)
# print(response)




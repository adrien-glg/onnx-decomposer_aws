import boto3
from datetime import datetime, timedelta
import pprint


cloudwatch_client = boto3.client('cloudwatch')


# response = cloudwatch_client.list_metrics(
#         Namespace='AWS/Lambda'
# )

yesterday = datetime.now() - timedelta(days=1)

response = cloudwatch_client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'id_586970858',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/Lambda',
                    'MetricName': 'Duration',
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




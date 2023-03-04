import boto3
from datetime import datetime, timedelta
import pprint

cloudwatch_client = boto3.client('cloudwatch')
# cloudwatch = boto3.resource('cloudwatch')
# metric = cloudwatch.Metric('namespace','name')

# response = cloudwatch_client.list_metrics()

yesterday = datetime.now() - timedelta(days=1)

response= cloudwatch_client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'q1',
            'Expression': "SELECT AVG(ExecutionTime) FROM SCHEMA(\"AWS/States\", StateMachineArn)",
            'Period': 300,
        },
    ],
    StartTime=yesterday,
    EndTime=datetime.now()
)

#pprint.pprint(response)
pprint.pprint(response['MetricDataResults'][0]['Values'])
# print(response)




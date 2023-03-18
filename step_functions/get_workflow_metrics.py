import boto3
from datetime import datetime, timedelta
import pprint

import utils

cloudwatch_client = boto3.client('cloudwatch')
# cloudwatch = boto3.resource('cloudwatch')
# metric = cloudwatch.Metric('namespace','name')

state_machine_arn = utils.get_state_machine_arn()
print("STATE MACHINE ARN: " + state_machine_arn + "\n")

# response = cloudwatch_client.list_metrics()

yesterday = datetime.now() - timedelta(days=1)

response = cloudwatch_client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'q1',
            'Expression': "SELECT AVG(ExecutionTime) FROM SCHEMA(\"AWS/States\", StateMachineArn) "
                          "WHERE StateMachineArn = '" + state_machine_arn + "'",
            'Period': 1  # The longer the period, the fewer values
        },
    ],
    StartTime=yesterday,
    EndTime=datetime.now()
)

#pprint.pprint(response)
print("AVG(ExecutionTime):")
pprint.pprint(response['MetricDataResults'][0]['Values'])
# print(response)




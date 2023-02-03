import boto3
import pprint


cloudwatch_client = boto3.client('cloudwatch')

# response = cloudwatch_client.list_metrics()

response = cloudwatch_client.list_metrics(
        Namespace='AWS/Lambda'
)

print(response)
# pprint.pprint(response)

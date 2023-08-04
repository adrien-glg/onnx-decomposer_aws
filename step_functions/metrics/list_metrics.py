import boto3


if __name__ == '__main__':
    cloudwatch_client = boto3.client('cloudwatch')

    response = cloudwatch_client.list_metrics(
        # Namespace='AWS/Lambda'
        Namespace='AWS/States'
    )

    response_metrics = response['Metrics']

    for i in range(len(response_metrics)):
        print(response_metrics[i]['MetricName'])

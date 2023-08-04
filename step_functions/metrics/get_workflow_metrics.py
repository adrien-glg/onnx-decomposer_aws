import boto3
from datetime import datetime, timedelta

from step_functions.deployment import utils


cloudwatch_client = boto3.client('cloudwatch')

state_machine_arn = utils.get_state_machine_arn()


def get_total_exec_times():
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

    execution_times = response['MetricDataResults'][0]['Values']
    return execution_times


def print_total_exec_times(execution_times):
    print("TOTAL EXECUTION TIME AVERAGES:")
    for time in execution_times:
        print(str(time) + " ms")


print("STATE MACHINE ARN: " + state_machine_arn + "\n")
exec_times = get_total_exec_times()
print_total_exec_times(exec_times)

import boto3
import json

iam = boto3.client('iam')
role_policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

# cloudwatch_role_policy = {
#     "Sid": "VisualEditor0",
#     "Effect": "Allow",
#     "Principal": {
#       "Service": "states.amazonaws.com"
#     },
#     "Action": "cloudwatch:*",
# }

response = iam.create_role(
  RoleName='StepFunctionsExecutionWithLogs',
  AssumeRolePolicyDocument=json.dumps(role_policy),
)
attach_lambda_policy_response = iam.attach_role_policy(
    RoleName='StepFunctionsExecutionWithLogs',
    PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaRole'
)
attach_cloudwatch_policy_response = iam.attach_role_policy(
    RoleName='StepFunctionsExecutionWithLogs',
    PolicyArn='arn:aws:iam::aws:policy/CloudWatchFullAccess'
)

print(response)
print(attach_lambda_policy_response)
print(attach_cloudwatch_policy_response)
#!/bin/bash

source project.config
LAMBDA_CONFIG_FILE="lambda_config/lambda_${PROJECT_NAME}.config"
source ${LAMBDA_CONFIG_FILE}
source constants.sh

echo "FUNCTION:" ${FUNCTION_NAME}
echo "EXECUTION_TIMEOUT:" ${EXECUTION_TIMEOUT}"s"
echo "FUNCTION_MEMORY:" ${FUNCTION_MEMORY}"MB"
echo

function_details=$(aws lambda list-functions --query "Functions[?FunctionName==\`${FUNCTION_NAME}\`]")
if [ ${#function_details} -gt 200 ]; then
    echo "Deleting old function..."
    aws lambda delete-function --function-name ${FUNCTION_NAME}
    echo "Deleted old function successfully"
fi

echo "Uploading deployment package to S3..."
aws s3 cp ${ZIP_PACKAGE_PATH} s3://${S3_BUCKET}
echo "Uploaded deployment package successfully"

echo "Deploying Lambda function..."
aws lambda create-function --function-name ${FUNCTION_NAME} \
--code S3Bucket=${S3_BUCKET},S3Key=${ZIP_PACKAGE} --handler ${LAMBDA_HANDLER}.lambda_handler --runtime python3.8 \
--role arn:aws:iam::426543810977:role/lambda-ex --timeout ${EXECUTION_TIMEOUT} --memory-size ${FUNCTION_MEMORY}
echo "Deployed Lambda function successfully"

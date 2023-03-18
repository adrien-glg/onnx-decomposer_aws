#!/bin/bash

source project.config
LAMBDA_CONFIG_FILE="lambda_config/lambda_${PROJECT_NAME}.config"
source ${LAMBDA_CONFIG_FILE}
source constants.sh

if [[ $# -eq 0 ]]
then
    echo "script usage: $0 -l <layer_index>"
    exit 1
fi


while getopts :l: flag
do
    case "${flag}" in
        l)
          layer_number=${OPTARG}
          ;;
    esac
done

INPUT_PAYLOAD="file://${EVENTS_PATH}/event${layer_number}.json"
OUTPUT_PAYLOAD_FULL="${EVENTS_PATH}/event$((${layer_number}+1))_full.json"
OUTPUT_PAYLOAD="${EVENTS_PATH}/event$((${layer_number}+1)).json"

aws lambda invoke --function-name ${FUNCTION_NAME} --cli-binary-format raw-in-base64-out --payload ${INPUT_PAYLOAD} ${OUTPUT_PAYLOAD_FULL}

cat ${OUTPUT_PAYLOAD_FULL} | jq .
cat ${OUTPUT_PAYLOAD_FULL} | jq .body > ${OUTPUT_PAYLOAD}



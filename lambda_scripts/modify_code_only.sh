#!/bin/bash

# USE THIS SCRIPT TO MODIFY CODE ONLY (INSIDE ZIP PACKAGE), AFTER RUNNING ./make_lambda_package.sh AT LEAST ONCE

source project.config
LAMBDA_CONFIG_FILE="lambda_config/lambda_${PROJECT_NAME}.config"
source ${LAMBDA_CONFIG_FILE}
source constants.sh

echo "FUNCTION:" ${FUNCTION_NAME}

unzip ${ZIP_PACKAGE_PATH} -d ${PACKAGE_PATH}/package

cd ${PACKAGE_PATH}/package
rm -r ${LAMBDA_HANDLER_PY} src ${IMAGE_FILE}
cd -

cp -r ${LAMBDA_CODE}/* ${INPUT_IMAGE_PATH} ${PACKAGE_PATH}/package

cd ${PACKAGE_PATH}/package
zip -r ../package.zip .
cd ..

mv package.zip ${ZIP_PACKAGE}

rm -r package

echo; echo "Modified successfully Lambda deployment package '" ${ZIP_PACKAGE} "'"





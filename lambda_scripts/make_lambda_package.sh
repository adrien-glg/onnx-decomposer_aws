#!/bin/bash

# DO NOT FORGET TO RUN THIS SCRIPT INSIDE A PYTHON VENV!!!

source project.config
LAMBDA_CONFIG_FILE="lambda_config/lambda_${PROJECT_NAME}.config"
source ${LAMBDA_CONFIG_FILE}
source constants.sh

echo "FUNCTION:" ${FUNCTION_NAME}; echo

########### INITIALIZATION ###########
if [[ -f "${ZIP_PACKAGE_PATH}" ]]; then
  rm ${ZIP_PACKAGE_PATH}
fi

if [[ ! -d ${PACKAGES_PATH} ]]; then
  mkdir ${PACKAGES_PATH}
fi

if [[ ! -d "${PACKAGE_PATH}" ]]; then
  mkdir ${PACKAGE_PATH}
fi


########### MAIN ###########
pip install -Iv --target ${PACKAGE_PATH}/package -r ${LAMBDA_REQUIREMENTS}

cp -r ${LAMBDA_CODE}/* ${INPUT_IMAGE_PATH} ${PACKAGE_PATH}/package

cd ${PACKAGE_PATH}/package
zip -r ../package.zip .
cd ..

mv package.zip ${ZIP_PACKAGE}

rm -r package

echo; echo ${ZIP_PACKAGE} "successfully created"

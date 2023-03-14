# onnx-decomposer_aws

## Package size conformity check

To perform package size conformity check, please follow these steps: 
[README_packagesize.md](README_packagesize.md)

## Initial configuration

First, make sure you have created the folder `lambda_code/projects/<projectname>` with these 3 project configuration files:
- `lambda_code/projects/<projectname>/<projectname>_config.ini`
- `lambda_code/projects/<projectname>/<projectname>_lambda.py`
- `lambda_code/projects/<projectname>/<projectname>_lambda_requirements.txt`

Then, you need to configure the following 2 files as needed:
- `lambda_code/projectname_config.ini`
- `lambda_scripts/project.config`

Finally, create the folder `models/<projectname>` and insert the input file(s).

## Lambda function deployment

Change directory:
```bash
cd lambda_scripts
```

Create a Python Virtual Environment (venv):
```bash
./create_python_venv.sh
```

You need to activate the virtual environment with `source venv/bin/activate` for the next steps.       
You can deactivate the virtual environment with `deactivate`.

Before creating the Lambda package, make sure `lambda_code/projectname_config.ini` and 
`lambda_scripts/project.config` have been configured correctly.

Create the deployment Lambda package:
```bash
./make_lambda_package.sh
```

Only if needed, once the package has been created a first time, you can easily apply code modifications with:                
<sub>NB: This command's purpose is only to save some time compared to making the Lambda package from scratch again.</sub>
```bash
./modify_code_only.sh
```

Deploy the Lambda function on AWS:
```bash
./deploy_lambda_function.sh
```

## Manual execution

Before invoking the Lambda function, make sure you have run the code locally.
A local execution will generate `events/event0.json` and will upload the correct ONNX slices to AWS S3.     
IMPORTANT: Repeat the above step every time you change the project or the number of slices.

To invoke the Lambda function (for the first layer, layer_index is `0`):
```bash
./invoke_lambda_function.sh -l <layer_index>
```
Run the command above as many times as there are layers.

## Automated execution with AWS Step Functions

Before invoking the Lambda function, make sure you have run the code locally.
A local execution will generate `events/event0.json` and will upload the correct ONNX slices to AWS S3.             
IMPORTANT: Repeat the above step every time you change the project or the number of slices.

From the `root` of the project (`onnx-decomposer_aws` folder), run the following command:
```bash
export PYTHONPATH=$PYTHONPATH:"$PWD":"$PWD/lambda_code"
cd step_functions
```

Create a role for Step Functions operations (you only need to run this command once and for all for your AWS account):
```bash
python3 grant_permissions.py
```
If you get an error warning about `"Role with name StepFunctionLambdaBasicExecution already exists"`, you can ignore it.

Before deployment, you need to configure the following file as needed:
- `step_functions/sfn_config.ini`


Deploy the workflow:
```bash
python3 deploy_workflow.py
```

Execute the workflow:
- Synchronously (waits for the results):
```bash
python3 execute_workflow_sync.py
```
- Asynchronously (only starts execution, does not wait for the result):
```bash
python3 execute_workflow_async.py [number_of_concurrent_executions]
```
<sub>NB: By default on AWS, concurrent executions quota for Lambda might be set to 10.
You can request a quota increase on this page: https://console.aws.amazon.com/servicequotas/home </sub>

## Metrics

See [README_metrics.md](README_metrics.md)

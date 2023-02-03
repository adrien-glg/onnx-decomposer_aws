# onnx-decomposer_aws

## Init Configuration

First, you need to configure the 2 following files as needed:
- `lambda_code/project_name.py`
- `lambda_scripts/project.config`

## Lambda Function Deployment

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

Before creating the Lambda package, make sure `lambda_scripts/project.config` and `lambda_code/project_name.py` have been configured correctly.

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

## Manual Execution

Before invoking the Lambda function, make sure you have run the code locally, so that `events/event0.json` has been generated correctly.   

To invoke the Lambda function (for the first layer, layer_index is `0`):
```bash
./invoke_lambda_function.sh -l <layer_index>
```
Run the command above as many times as there are layers.

## Automated Execution with AWS Step Functions

Before execution, make sure you have run the code locally, so that `events/event0.json` has been generated correctly. 

From `root` (`onnx-decomposer_aws` folder), run the following command:
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
- `step_functions/sfn_config.py`


Deploy the workflow:
```bash
python3 deploy_workflow.py
```

Execute the workflow:
```bash
python3 execute_workflow.py
```

[//]: # (Get results:)

[//]: # (```bash)

[//]: # (python3 get_results.py)

[//]: # (```)


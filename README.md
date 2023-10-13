# ONNX Decomposer (AWS)

**ONNX Decomposer for the Deployment of Machine Learning Models on Serverless**

This project is divided into two repositories: 
- [onnx-decomposer_local](https://github.com/adrien-glg/onnx-decomposer_local) for local inference
- [onnx-decomposer_aws](https://github.com/adrien-glg/onnx-decomposer_aws) for Serverless inference on AWS

This is part of a Software Engineering Master's Thesis, carried out at the University of Amsterdam (UvA).
You will find all the details about this project in the [Thesis Report](https://dspace.uba.uva.nl/bitstreams/7b31ef71-cf20-4396-9c27-56f86f0b7f55/download).

## Thesis Abstract

In recent years, Serverless computing has emerged as a persuasive paradigm aiming to reshape the cloud
computing landscape considerably. Serverless offers a scalable and cost-effective deployment model where
users can run applications without the need to manage or provision servers. The underlying infrastructure
is entirely abstracted and has the ability to scale automatically in a flexible manner, while the users are
charged exclusively for the resources they use. In parallel, we have witnessed a surge in the adoption
of Artificial Intelligence and Machine Learning (ML) technologies in various application domains. Since
Serverless architectures are not tailored to address the unique challenges posed by resource-intensive
jobs, combining ML with Serverless proves to be a complex undertaking.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this thesis, we propose a solution for deploying ML models on Serverless platforms, specifically for
inference jobs. Our model-agnostic approach is based on a flexible decomposition of such models into sub-models,
referred to as slices, and the execution of inferences in a workflow of Serverless functions. We rely
on conducting a thorough investigation of the limitations affecting the most popular Serverless platforms
on the market and devising strategies to overcome them. Our experimental evaluations are performed
on AWS, considering the ONNX open source format for ML model representation. Our results show
that our decomposition method enables running ML inference on Serverless, regardless of the model size,
benefiting from the high scalability of this architecture while lowering the strain on computing resources
such as required runtime memory.

## Conformity check: Check package size violation

To perform the conformity check **Check package size violation**, please follow these steps: 
[README_packagesize.md](README_packagesize.md)

## Initial configuration

Configure the following files as needed:       
- `lambda_code/projects/<projectname>/<projectname>_config.ini`
- `lambda_code/projects/<projectname>/<projectname>_lambda_requirements.txt`
- `lambda_code/projects/<projectname>/<projectname>_lambda_steps.py`

Then, configure the following files as needed:          
- `lambda_code/general_config.ini`
- `lambda_scripts/project.config`
- `lambda_scripts/lambda_config/lambda_<projectname>.config`

Finally, copy the input file(s) to the folder `models/<projectname>`.

## Lambda function deployment

First, create a Lambda deployment package by following the steps in the following section:
[making-lambda-deployment-package](README_packagesize.md#making-lambda-deployment-package)

Deploy the Lambda function on AWS:
```bash
./deploy_lambda_function.sh
```

## Serverless execution with manual testing

Before invoking the Lambda function, make sure you have run the code locally with the same project and the same
number of slices. These steps are described in the following repository: [onnx-decomposer_local](https://github.com/adrien-glg/onnx-decomposer_local).          
A local execution will upload to AWS S3 the ONNX slices generated during the model decomposition and
will generate the file `events/event0.json`.    
:warning: Repeat the above step every time you change the project or the number of slices.

To invoke the Lambda function (for the first layer, `layer_index` is `0`):    
<sub>NB: Run this command for each layer one by one. Run it as many times as there are layers</sub>.
```bash
./invoke_lambda_function.sh -l <layer_index>
```

## Automated Serverless execution with AWS Step Functions

Before starting an inference, make sure you have run the code locally with the same project and the same
number of slices.       
A local execution will upload to AWS S3 the ONNX slices generated during the model decomposition and
will generate the file `events/event0.json`.    
:warning: Repeat the above step every time you change the project or the number of slices.

From the `root` of the project (`onnx-decomposer_aws` folder), run the following command:
```bash
export PYTHONPATH=$PYTHONPATH:"$PWD":"$PWD/lambda_code"
cd step_functions/deployment
```

Create a role for Step Functions operations (you only need to run this command once and for all for your AWS account):
```bash
python3 grant_permissions.py
```
If you get the error `"Role with name StepFunctionLambdaBasicExecution already exists"`, you can ignore it.

Deploy the workflow:
```bash
python3 deploy_workflow.py
```

Run inferences by executing the workflow:
- Synchronously (waits for the results):
```bash
python3 execute_workflow_sync.py
```
- Asynchronously (only starts the execution, does not wait for the results):
```bash
python3 execute_workflow_async.py [number_of_concurrent_executions]
```
You can run multiple batches of executions separated by 30-second pauses with:
```bash
python3 execute_workflow_async.py [number_of_executions_batch1] [number_of_executions_batch2] [...]
```
<sub>NB: By default on AWS, the concurrent executions quota for Lambda might be set to 10.
You can request a quota increase on this page: https://console.aws.amazon.com/servicequotas/home </sub>

## Metrics

For metrics collection, see: [README_metrics.md](README_metrics.md)

## References

This project includes code and content from the following sources:
- [tensorflow-onnx](https://github.com/onnx/tensorflow-onnx/)

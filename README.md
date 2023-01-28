# onnx-decomposer_aws

```bash
cd src/aws
```

```bash
./create_python_venv.sh
source venv/bin/activate
```

Before creating the Lambda package, make sure `config.sh` and `project_name.py` have been configured correctly.
Create the deployment Lambda package:
```bash
./make_lambda_package.sh
```

Once the package has been created a first time, you can easily apply code modifications with:
```bash
./modify_code_only.sh
```
<small>NB: This command's purpose is only to save some time compared to making the Lambda package again</small>

To deploy the Lambda function on AWS:
```bash
./deploy_lambda_function.sh
```

Before invoking the Lambda function, make sure you have run the code locally, so that `event0.json` is the correct one.
To invoke the Lambda function (run as many times as there are layers):
```bash
./invoke_lambda_function.sh -l <layer_number>
```


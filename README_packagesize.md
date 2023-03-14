# Package size conformity check

## Initial configuration

First, make sure you have created the folder `lambda_code/projects/<projectname>` with these 3 project configuration files:         
<sub>(NB: Since we are only testing package size, configuration of `NUMBER_OF_SLICES` and `S3_BUCKET` are not needed
here. You can configure them later.)</sub>
- `lambda_code/projects/<projectname>/<projectname>_config.ini`
- `lambda_code/projects/<projectname>/<projectname>_lambda.py`
- `lambda_code/projects/<projectname>/<projectname>_lambda_requirements.txt`

Then, you need to configure the 2 following files as needed:       
<sub>(NB: Since we are only testing package size, there is no need to configure `NUMBER_OF_SLICES`, `S3_BUCKET`, 
`EXECUTION_TIMEOUT` and `FUNCTION_MEMORY`. You can configure them later.)</sub>
- `lambda_code/projectname_config.ini`
- `lambda_scripts/project.config`

## Making package

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

## Checking package size

From the `root` of the project (`onnx-decomposer_aws` folder), run the following commands:
```bash
export PYTHONPATH=$PYTHONPATH:"$PWD":"$PWD/utils"
cd utils
```

Check package size:
```bash
python3 main_packagesize.py
```
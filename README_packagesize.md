# Package size conformity check

## Initial configuration

If not already done, configure the following files as needed:       
<sub>NB: Since we are only testing the package size, the configuration of `NUMBER_OF_SLICES` and `S3_BUCKET` are not
required here. You can configure them later.</sub>
- `lambda_code/projects/<projectname>/<projectname>_config.ini`
- `lambda_code/projects/<projectname>/<projectname>_lambda_requirements.txt`
- `lambda_code/projects/<projectname>/<projectname>_lambda_steps.py`

Then, configure the following files as needed:     
<sub>NB: Again, no need to configure `NUMBER_OF_SLICES`.</sub>
- `lambda_code/general_config.ini`
- `lambda_scripts/project.config`

## Making Lambda deployment package

Change directory:
```bash
cd lambda_scripts
```

Create a Python Virtual Environment (venv):
```bash
./create_python_venv.sh
```

You need to activate the virtual environment with `source venv/bin/activate` for the following steps.       
Later, you can deactivate the virtual environment with `deactivate`.

Before creating the Lambda package, make sure `lambda_code/general_config.ini` and 
`lambda_scripts/project.config` have been configured correctly.

Create the Lambda deployment package:
```bash
./make_lambda_package.sh
```

Only if needed, once the package has been created a first time, you can easily apply code modifications with:                
<sub>NB: This command's purpose is only to save some time compared to making the Lambda package from scratch again.</sub>
```bash
./modify_code_only.sh
```

## Conformity check: Checking package size

From the `root` of the project (`onnx-decomposer_aws` folder), run the following commands:
```bash
export PYTHONPATH=$PYTHONPATH:"$PWD"
cd conformity_checks
```

Check package size:
```bash
python3 check_package_size.py
```

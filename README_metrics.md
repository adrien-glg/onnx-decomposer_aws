## Metrics

From the `root` of the project (`onnx-decomposer_aws` folder), run the following command:
```bash
export PYTHONPATH=$PYTHONPATH:"$PWD":"$PWD/lambda_code"
cd step_functions/metrics
```

There are 3 modes available to save metrics:
- `executions`: Execution time and memory usage per slice execution
- `timestamps`: Execution time and memory usage per slice execution with associated timestamps
- `perslice`: Execution time and memory usage per slice execution within each workflow inference

Save metrics:
```bash
python3 save_lambda_metrics.py <mode>
```

Plot metrics:
```bash
python3 plot_lambda_metrics.py <mode>
```

Plot workflow total execution time as a function of the number of slices:
```bash
python3 plot_workflow_total_exec_times.py
```
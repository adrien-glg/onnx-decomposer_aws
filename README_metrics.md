## Metrics

From the `root` of the project (`onnx-decomposer_aws` folder), run the following command:
```bash
export PYTHONPATH=$PYTHONPATH:"$PWD":"$PWD/lambda_code"
cd step_functions/metrics
```

There are 3 modes available to save metrics:
- `executions`
- `perslice`
- `timestamps`

Save metrics:
```bash
python3 save_lambda_metrics.py <mode>
```

```bash
python3 plot_lambda_metrics.py  # TODO
```
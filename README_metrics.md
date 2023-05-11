## Metrics

From the `root` of the project (`onnx-decomposer_aws` folder), run the following command:
```bash
export PYTHONPATH=$PYTHONPATH:"$PWD":"$PWD/lambda_code"
cd step_functions/metrics
```

```bash
python3 save_lambda_metrics.py  # TODO
```

```bash
python3 plot_lambda_metrics.py  # TODO
```
PROJECT_NAME = "efficientdet"
ONNX_MODEL = "efficientdet-d2.onnx"
INPUT_IMAGE = "img_efficientdet.png"
INPUT_LIST_START = ["image_arrays:0"]
OUTPUT_LIST_END = ['detections:0']
S3_BUCKET = "onnx-efficientdet-bucket"

NUMBER_OF_SLICES = 5



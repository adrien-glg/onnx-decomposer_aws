PROJECT_NAME = "mobiledet"
ONNX_MODEL = "mobiledet.onnx"
INPUT_IMAGE = "img_resized.npy"
INPUT_LIST_START = ['normalized_input_image_tensor']
OUTPUT_LIST_END = ["TFLite_Detection_PostProcess", "TFLite_Detection_PostProcess:1",
                   "TFLite_Detection_PostProcess:2", "TFLite_Detection_PostProcess:3"]
S3_BUCKET = "onnx-mobiledet-bucket"

NUMBER_OF_SLICES = 2



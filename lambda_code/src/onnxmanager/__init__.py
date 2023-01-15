import importlib
from src import generic_constants
constants = importlib.import_module(generic_constants.CONSTANTS_MODULE, package=None)

# MODEL_PATH = "../models/" + constants.PROJECT_NAME + "/" + constants.ONNX_MODEL
# JSON_ROOT_PATH = "data/"
# JSON_PAYLOAD_PATH = "data/payload.json"
# DICTIONARY_PATH = "data/filenames_dictionary.json"
# EVENT_PATH = "data/event.json"
# SLICES_PATH = "../models/" + constants.PROJECT_NAME + "/slices/"
# SLICES_PATH_S3 = "models/slices/"

MODEL_PATH = constants.ONNX_MODEL
JSON_ROOT_PATH_S3 = "data/"
JSON_ROOT_PATH = "/tmp/" + JSON_ROOT_PATH_S3
JSON_PAYLOAD_PATH_S3 = "data/payload.json"
JSON_PAYLOAD_PATH = "/tmp/" + JSON_PAYLOAD_PATH_S3
DICTIONARY_PATH_S3 = "data/filenames_dictionary.json"
DICTIONARY_PATH = "/tmp/" + DICTIONARY_PATH_S3
SLICES_PATH_S3 = "models/slices/"
SLICES_PATH = "/tmp/" + SLICES_PATH_S3
SLICES_PATH_ROOT = "/tmp/models"



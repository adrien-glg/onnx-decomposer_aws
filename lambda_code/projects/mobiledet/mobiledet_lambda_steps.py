import numpy as np
from src import constants
from src.jsonmanager import json_manager


def get_preprocessed_input():
    img = np.load(constants.PREPROCESSED_INPUT)
    img = img.astype("float32")
    return img


def get_result():
    result = json_manager.get_payload_content("TFLite_Detection_PostProcess")
    result = result[0][0]
    return result

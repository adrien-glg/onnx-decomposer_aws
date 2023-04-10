import numpy as np
from src import constants
from src.jsonmanager import json_manager


def get_preprocessed_input():
    input_array = np.load(constants.PREPROCESSED_INPUT)
    input_float = input_array.astype("float32")
    img = np.array([input_float])
    return img


def get_result():
    result = json_manager.get_payload_content("predictions")
    result = result[0][0]
    return result

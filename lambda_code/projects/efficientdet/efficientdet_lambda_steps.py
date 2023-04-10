import numpy as np
from src import constants
from src.jsonmanager import json_manager


def get_preprocessed_input():
    images = []
    for f in [constants.PREPROCESSED_INPUT]:
        images.append(np.array(Image.open(f)))
    img = np.array(images, dtype='uint8')
    return img


def get_result():
    result = json_manager.get_payload_content("detections:0")
    result = result[0][0]
    return result

from subprocess import call
import numpy as np
from PIL import Image

from src.jsonmanager import json_manager
from src.inference import first_slice, other_slices
from src.s3manager import s3_manager

import importlib
from src import generic_constants
constants = importlib.import_module(generic_constants.CONSTANTS_MODULE, package=None)


def lambda_handler(event, context):
    number_of_slices = event['number_of_slices']
    slice_index = event['next_slice_index']
    payload_index = event['next_payload_index']
    inputs = event['inputs']
    outputs = event['outputs']

    s3_manager.download_onnx_slice(slice_index)

    if slice_index == 0:
        s3_manager.delete_dictionary()  # from previous executions
        s3_manager.delete_payloads_from_s3()
        s3_manager.init_dictionary_on_s3()
        ### MOBILEDET:
        # img = np.load(constants.INPUT_IMAGE)
        # img = img.astype("float32")
        ### END MOBILEDET
        ### EFFICIENTDET:
        images = []
        for f in [constants.INPUT_IMAGE]:
            images.append(np.array(Image.open(f)))
        img = np.array(images, dtype='uint8')
        ### END EFFICIENTDET
        first_slice.run(img, outputs)
    else:
        s3_manager.download_dictionary()
        other_slices.run(slice_index, payload_index, inputs, outputs)

    s3_manager.upload_dictionary_to_s3()

    s3_manager.upload_payloads_to_s3()

    next_slice_index = slice_index + 1
    next_payload_index = json_manager.get_next_payload_index()

    if next_slice_index == constants.NUMBER_OF_SLICES:
        ### MOBILEDET:
        # result = json_manager.get_payload_content("TFLite_Detection_PostProcess")
        ### EFFICIENTDET:
        result = json_manager.get_payload_content("detections:0")
        output_event = {"keep_going": False, "result": result[0][0]}
    else:
        output_event = {"keep_going": True, "number_of_slices": number_of_slices, "next_slice_index": next_slice_index,
                        "next_payload_index": next_payload_index, "inputs": inputs, "outputs": outputs}

    # call('rm -rf /tmp/*', shell=True)
    # call('rm -rf /tmp/..?* /tmp/.[!.]* /tmp/*', shell=True)
    call('rm -rf /tmp/data/payload*', shell=True)
    call('rm -rf /tmp/models/*', shell=True)

    return {
        'statusCode': 200,
        'body': output_event
    }
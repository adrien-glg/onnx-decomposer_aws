from subprocess import call

from src.inference import first_slice, other_slices
from src.s3manager import s3_manager
from src import constants

import importlib
project_steps = importlib.import_module(constants.PROJECT_STEPS_MODULE, package=None)


def lambda_handler(event, context):
    # Read the input event
    number_of_slices = event['number_of_slices']
    slice_index = event['next_slice_index']
    inputs = event['inputs']
    outputs = event['outputs']

    # Download the required ONNX slice from AWS S3
    s3_manager.download_onnx_slice(slice_index)

    if slice_index == 0:
        # Delete the remaining files from previous executions and initialize the dictionary
        s3_manager.delete_dictionary()
        s3_manager.delete_payloads_from_s3()
        s3_manager.init_dictionary_on_s3()

        # Load the input data
        img = project_steps.get_preprocessed_input()

        # Run the inference for the first slice
        first_slice.run(img, slice_index, outputs)

    else:
        # Download the dictionary from AWS S3
        s3_manager.download_dictionary()

        # Run the inference for any other slice, not the first slice
        other_slices.run(slice_index, inputs, outputs)

    # Upload the dictionary and payloads to AWS S3
    s3_manager.upload_dictionary_to_s3()
    s3_manager.upload_payloads_to_s3()
    next_slice_index = slice_index + 1

    # Get the results and prepare the output events
    if next_slice_index == constants.NUMBER_OF_SLICES:
        result = project_steps.get_result()
        output_event = {"keep_going": False, "result": result}
    else:
        output_event = {"keep_going": True, "number_of_slices": number_of_slices, "next_slice_index": next_slice_index,
                        "inputs": inputs, "outputs": outputs}

    # Clear AWS Lambda cache (tmp folder)
    call('rm -rf /tmp/data/payload*', shell=True)
    call('rm -rf /tmp/models/*', shell=True)

    return {
        'statusCode': 200,
        'body': output_event
    }

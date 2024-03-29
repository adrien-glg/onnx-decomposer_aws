import os
import onnx

from src import onnxmanager
from src import constants


def get_slice_path(slice_index):
    # AWS
    if not os.path.exists(onnxmanager.SLICES_PATH_ROOT):
        os.mkdir(onnxmanager.SLICES_PATH_ROOT)
    # END AWS
    directory = onnxmanager.SLICES_PATH
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory + constants.PROJECT_NAME + "_slice" + str(slice_index).zfill(2) + ".onnx"


def get_slice_path_s3(slice_index):
    directory = onnxmanager.SLICES_PATH_S3
    return directory + constants.PROJECT_NAME + "_slice" + str(slice_index).zfill(2) + ".onnx"


def extract_slice(model_slice_path, input_list, output_list):
    onnx.utils.extract_model(onnxmanager.MODEL_PATH, model_slice_path, input_list, output_list)


def extract_model_slices(input_lists, output_lists):
    for slice_index in range(constants.NUMBER_OF_SLICES):
        model_slice_path = get_slice_path(slice_index)
        extract_slice(model_slice_path, input_lists[slice_index], output_lists[slice_index])

import os

from step_functions.deployment import sfn_constants


def get_csv_filenames(timestamps=False):
    filenames_list = os.listdir(sfn_constants.METRICS_FOLDER)
    if timestamps:
        filenames_list = [file for file in filenames_list if "timestamps" in file]
    else:
        filenames_list = [file for file in filenames_list if "executions" in file]
    return filenames_list


def get_label(filename):
    number_of_slices = filename.split('_')[1]
    if number_of_slices == "1":
        label = number_of_slices + " slice"
    else:
        label = number_of_slices + " slices"
    return label

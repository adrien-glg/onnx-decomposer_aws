import os

from step_functions.deployment import sfn_constants


def get_csv_filenames(mode):
    filenames_list = os.listdir(sfn_constants.METRICS_FOLDER)
    if mode == "executions":
        filenames_list = [file for file in filenames_list if "executions" in file]
    elif mode == "perslice":
        filenames_list = [file for file in filenames_list if "perslice" in file]
    elif mode == "timestamps":
        filenames_list = [file for file in filenames_list if "timestamps" in file]
    elif mode == "initdurations":
        filenames_list = [file for file in filenames_list if "initdurations" in file]
    return filenames_list


def get_label(filename):
    number_of_slices = filename.split('_')[1]
    number_of_slices = str(int(number_of_slices))
    if number_of_slices == "1":
        label = "Non-sliced model"
    else:
        label = number_of_slices + " slices"
    return label

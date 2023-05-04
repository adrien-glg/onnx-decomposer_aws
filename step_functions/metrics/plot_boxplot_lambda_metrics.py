import matplotlib.pyplot as plt
import csv
import os

from step_functions.deployment import sfn_constants


def get_csv_files():
    return os.listdir(sfn_constants.METRICS_FOLDER)


# FUNCTION NAMES = CSV FILES WO EXTENSION
def get_function_names():
    function_names = []
    csv_files = get_csv_files()
    for i in range(len(csv_files)):
        function_names += [os.path.splitext(csv_files[i])[0]]
    return function_names


def get_plot_data(header_index):
    data = []
    csv_files = get_csv_files()
    expected_csv_file = sfn_constants.FUNCTION_NAME + ".csv"

    # for i in range(len(csv_files)):
    #     with open(sfn_constants.METRICS_FOLDER + csv_files[i], 'r') as csvfile:
    if expected_csv_file in csv_files:
        with open(sfn_constants.METRICS_FOLDER + expected_csv_file, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            next(lines)
            for row in lines:
                slice_number = int(row[1])
                if len(data) < slice_number + 1:
                    data += [[]]
                data[slice_number] += [float(row[header_index])]
    return data


def plot_duration():
    duration_index = sfn_constants.CSV_HEADERS.index(sfn_constants.DURATION_TAG)
    data = get_plot_data(duration_index)
    function_names = get_function_names()

    plt.subplot(1, 2, duration_index - 1)
    plt.boxplot(data)
    # plt.xticks(range(len(data)))
    plt.xlabel("Slice number")
    plt.ylabel(sfn_constants.DURATION_TAG)
    # plt.title('Execution time (' + sfn_constants.FUNCTION_NAME + ")", fontsize=20)
    plt.grid()
    plt.legend()


def plot_used_memory():
    used_memory_index = sfn_constants.CSV_HEADERS.index(sfn_constants.USED_MEMORY_TAG)
    data = get_plot_data(used_memory_index)
    function_names = get_function_names()

    plt.subplot(1, 2, used_memory_index - 1)
    plt.boxplot(data)
    # plt.xticks(range(1, len(Y)+1), function_names)
    plt.xlabel("Slice number")
    plt.ylabel(sfn_constants.USED_MEMORY_TAG)
    # plt.title('Memory (' + sfn_constants.FUNCTION_NAME + ")", fontsize=20)
    plt.grid()
    plt.legend()


if __name__ == "__main__":
    plot_duration()
    plot_used_memory()
    mng = plt.get_current_fig_manager()
    mng.resize(1600, 600)
    plt.show()

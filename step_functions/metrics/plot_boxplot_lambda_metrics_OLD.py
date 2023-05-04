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
    X, Y = [], []
    csv_files = get_csv_files()

    for i in range(len(csv_files)):
        with open(sfn_constants.METRICS_FOLDER + csv_files[i], 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            x, y = [], []
            next(lines)
            for row in lines:
                x += [int(row[1])]
                y += [float(row[header_index])]
            X += [x]
            Y += [y]
    return X, Y


def plot_duration():
    duration_index = sfn_constants.CSV_HEADERS.index(sfn_constants.DURATION_TAG)
    Y = get_plot_data(duration_index)[1]
    function_names = get_function_names()

    plt.subplot(1, 2, duration_index - 1)
    plt.boxplot(Y)
    plt.xticks(range(1, len(Y)+1), function_names)
    plt.ylabel(sfn_constants.DURATION_TAG)
    # plt.title('Execution time', fontsize=20)
    plt.grid()
    plt.legend()


def plot_used_memory():
    used_memory_index = sfn_constants.CSV_HEADERS.index(sfn_constants.USED_MEMORY_TAG)
    Y = get_plot_data(used_memory_index)[1]
    function_names = get_function_names()

    plt.subplot(1, 2, used_memory_index - 2)
    plt.boxplot(Y)
    plt.xticks(range(1, len(Y)+1), function_names)
    plt.ylabel(sfn_constants.USED_MEMORY_TAG)
    # plt.title('Memory', fontsize=20)
    plt.grid()
    plt.legend()


if __name__ == "__main__":
    plot_duration()
    plot_used_memory()
    mng = plt.get_current_fig_manager()
    mng.resize(1600, 600)
    plt.show()

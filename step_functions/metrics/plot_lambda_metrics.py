import matplotlib.pyplot as plt
import csv
import os
import numpy as np

from step_functions.deployment import sfn_constants
import helpers


def get_plot_data(header_index):
    X, Y = [], []
    csv_files = helpers.get_csv_filenames()

    for i in range(len(csv_files)):
        with open(sfn_constants.METRICS_FOLDER + csv_files[i], 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            x, y = [], []
            next(lines)
            for row in lines:
                x += [int(row[0])]
                y += [float(row[header_index])]
            X += [x]
            Y += [y]
    return X, Y


def get_total_exec_time():
    functions, times = [], []
    text = "Total Execution Time Average:\n"
    with open(sfn_constants.TOTAL_TIME_FILEPATH, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            functions += [row[0]]
            times += [int(float(row[1]))]
    for i in range(len(functions)):
        text += functions[i] + ": " + str(times[i]) + " ms\n"
    return text


def plot_duration():
    duration_index = sfn_constants.CSV_HEADERS.index(sfn_constants.DURATION_TAG) - 1
    X, Y = get_plot_data(duration_index)
    exec_times_text = get_total_exec_time()
    csv_files = helpers.get_csv_filenames()

    plt.subplot(2, 1, duration_index)
    for i in range(len(csv_files)):
        plt.plot(X[i], Y[i], marker=sfn_constants.MARKERS[i], label=os.path.splitext(csv_files[i])[0])
    # plt.xticks(range(X[-1][0], X[-1][-1]+1))
    plt.xlabel(sfn_constants.CSV_HEADERS[0])
    plt.ylabel(sfn_constants.DURATION_TAG)
    # plt.title(sfn_constants.PROJECT_NAME.upper() + '\n\nExecution time', fontsize=20)
    # plt.annotate(exec_times_text, xy=(0.05, 0.80), xycoords='axes fraction')
    plt.annotate(exec_times_text, xy=(0, 1), xytext=(12, 50), va='top',
                 xycoords='axes fraction', textcoords='offset points')
    # plt.axvline(x=50, color='r')
    # plt.axvline(x=100, color='r')
    plt.grid()
    plt.legend()


def plot_used_memory():
    used_memory_index = sfn_constants.CSV_HEADERS.index(sfn_constants.USED_MEMORY_TAG) - 1
    X, Y = get_plot_data(used_memory_index)
    csv_files = helpers.get_csv_filenames()

    plt.subplot(2, 1, used_memory_index)
    for i in range(len(csv_files)):
        plt.plot(X[i], Y[i], marker=sfn_constants.MARKERS[i], label=os.path.splitext(csv_files[i])[0])
    # plt.xticks(range(X[-1][0], X[-1][-1]+1))
    plt.xlabel(sfn_constants.CSV_HEADERS[0])
    plt.ylabel(sfn_constants.USED_MEMORY_TAG)
    # plt.title('Memory', fontsize=20)
    # plt.axvline(x=50, color='r')
    # plt.axvline(x=100, color='r')
    plt.grid()
    # plt.legend()


if __name__ == "__main__":
    plot_duration()
    plot_used_memory()
    mng = plt.get_current_fig_manager()
    mng.resize(1600, 1000)
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    plt.show()

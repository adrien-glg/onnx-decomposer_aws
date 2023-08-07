import csv
import sys
import subprocess
import matplotlib.pyplot as plt

from step_functions.deployment import sfn_constants
import helpers


def get_plot_data(selected_mode, header_index):
    X, Y = [], []
    csv_files = helpers.get_csv_filenames(selected_mode)

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


def get_plot_data_perslice(header_index):
    data = []
    csv_files = helpers.get_csv_filenames("perslice")
    expected_csv_file = ""
    for file in csv_files:
        if file.startswith(sfn_constants.FUNCTION_NAME):
            expected_csv_file = file

    if expected_csv_file in csv_files:
        with open(sfn_constants.METRICS_FOLDER + expected_csv_file, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            next(lines)
            for row in lines:
                slice_number = int(row[1])
                if len(data) < slice_number:
                    data += [[]]
                data[slice_number - 1] += [float(row[header_index])]
    return data


def offset_timestamps(timestamps_lists):
    for i in range(len(timestamps_lists)):
        first_timestamp = timestamps_lists[i][0]
        for j in range(len(timestamps_lists[i])):
            timestamps_lists[i][j] -= first_timestamp


def plot_duration(selected_mode, csv_headers):
    duration_index = csv_headers.index(sfn_constants.DURATION_TAG)
    X, Y = get_plot_data(selected_mode, duration_index)
    if selected_mode == "timestamps":
        offset_timestamps(X)
    csv_files = helpers.get_csv_filenames(selected_mode)

    plt.subplot(2, 1, duration_index)
    for i in range(len(csv_files)):
        label = helpers.get_label(csv_files[i])
        plt.plot(X[i], Y[i], marker=sfn_constants.MARKERS[i], linestyle='-', label=label)
    plt.ylabel(sfn_constants.DURATION_TAG)
    plt.grid()
    plt.legend(bbox_to_anchor=(1.0, 1.0), loc='center')


def plot_duration_perslice():
    duration_index = sfn_constants.CSV_HEADERS_PERSLICE.index(sfn_constants.DURATION_TAG)
    data = get_plot_data_perslice(duration_index)

    plt.subplot(2, 1, duration_index - 1)
    plt.boxplot(data)
    plt.ylabel(sfn_constants.DURATION_TAG)
    plt.grid()


def plot_used_memory(selected_mode, csv_headers):
    used_memory_index = csv_headers.index(sfn_constants.USED_MEMORY_TAG)
    X, Y = get_plot_data(selected_mode, used_memory_index)
    if selected_mode == "timestamps":
        offset_timestamps(X)
    csv_files = helpers.get_csv_filenames(selected_mode)

    plt.subplot(2, 1, used_memory_index)
    for i in range(len(csv_files)):
        plt.plot(X[i], Y[i], marker=sfn_constants.MARKERS[i], linestyle='-')
    plt.xlabel(csv_headers[0])
    plt.ylabel(sfn_constants.USED_MEMORY_TAG)
    plt.grid()


def plot_used_memory_perslice():
    used_memory_index = sfn_constants.CSV_HEADERS_PERSLICE.index(sfn_constants.USED_MEMORY_TAG)
    data = get_plot_data_perslice(used_memory_index)

    plt.subplot(2, 1, used_memory_index - 1)
    plt.boxplot(data)
    plt.xlabel("Slice number")
    plt.ylabel(sfn_constants.USED_MEMORY_TAG)
    plt.grid()


if __name__ == '__main__':
    error_message = "Please enter a correct mode as argument: executions, timestamps, perslice"
    if len(sys.argv) != 2:
        raise Exception(error_message)
    else:
        mode = sys.argv[1]
        print("PROJECT: " + sfn_constants.PROJECT_NAME + ", " + str(sfn_constants.NUMBER_OF_SLICES) + " slice(s)\n")
        print("MODE: " + mode + "\n")
        print("Plotting metrics...")
        if mode == "perslice":
            figure_filename = sfn_constants.FIGURE_FILE_PERSLICE
            plot_duration_perslice()
            plot_used_memory_perslice()
        else:
            if mode == "executions":
                headers = sfn_constants.CSV_HEADERS_EXECUTIONS
                figure_filename = sfn_constants.FIGURE_FILE_EXECUTIONS
            elif mode == "timestamps":
                headers = sfn_constants.CSV_HEADERS_TIMESTAMPS
                figure_filename = sfn_constants.FIGURE_FILE_TIMESTAMPS
            else:
                raise Exception(error_message)
            plot_duration(mode, headers)
            plot_used_memory(mode, headers)
        plt.savefig(figure_filename, bbox_inches='tight')
        # subprocess.call(["xdg-open", figure_filename])
        plt.show()

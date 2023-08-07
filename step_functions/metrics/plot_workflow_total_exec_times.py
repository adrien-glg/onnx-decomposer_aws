import matplotlib.pyplot as plt
import csv

from step_functions.deployment import sfn_constants


def get_plot_data_total_exec_times(project_name):
    functions, slices, times = [], [], []
    metrics_folder = "../saved_metrics/" + project_name + "/"
    total_time_filepath = metrics_folder + project_name + '_total_exec_times.csv'
    with open(total_time_filepath, 'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        next(lines)
        for row in lines:
            functions += [row[0]]
            times += [int(float(row[1]))]
        for i in range(len(functions)):
            function_strings = functions[i].split("_")
            slices += [int(function_strings[1])]
    return slices, times


def plot_total_exec_times(project_names):
    full_X = []
    for project in project_names:
        X, Y = get_plot_data_total_exec_times(project)
        plt.plot(X, Y, marker="o", linestyle="-", label=project)
        full_X += X
    plt.xticks(range(1, max(full_X) + 1, 1))
    plt.xlabel("Number of slices")
    plt.ylabel("Total Execution Time Average (ms)")
    plt.grid()
    plt.legend(loc='upper right', framealpha=1)


if __name__ == "__main__":
    plot_total_exec_times(["mobiledet", "resnet50", "efficientdet"])
    mng = plt.get_current_fig_manager()
    mng.resize(1600, 1000)
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.4)
    plt.savefig(sfn_constants.METRICS_FOLDER + sfn_constants.PROJECT_NAME + "_exec_figure.pdf")
    plt.show()


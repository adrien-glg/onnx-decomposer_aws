from configparser import ConfigParser


config_parser = ConfigParser()

config_parser.read('../../lambda_code/general_config.ini')
PROJECT_NAME = config_parser.get('project', 'project_name')
NUMBER_OF_SLICES = config_parser.getint('project', 'number_of_slices')

config_parser.read('../lambda_code/projects/' + PROJECT_NAME + "/" + PROJECT_NAME + "_config.ini")

if NUMBER_OF_SLICES == 1:
    FUNCTION_NAME = PROJECT_NAME + "_01_slice"
else:
    FUNCTION_NAME = PROJECT_NAME + "_" + str(NUMBER_OF_SLICES).zfill(2) + "_slices"
STATE_MACHINE_NAME = FUNCTION_NAME + "_StateMachine"
EVENT0 = "../../events/event0.json"
STATE_MACHINE_ARN_FILE = "../outputs/state_machine_arn.txt"
EXECUTION_ARN_FILE = "../outputs/execution_arn.txt"

# METRICS
METRICS_FOLDER = "../saved_metrics/" + PROJECT_NAME + "/"
METRICS_FILE = METRICS_FOLDER + FUNCTION_NAME + '_executions.csv'
METRICS_FILE_PERSLICE = METRICS_FOLDER + FUNCTION_NAME + '_perslice.csv'
METRICS_FILE_TIMESTAMPS = METRICS_FOLDER + FUNCTION_NAME + '_timestamps.csv'
METRICS_FILE_INITDURATIONS = METRICS_FOLDER + FUNCTION_NAME + '_initdurations.csv'
FIGURE_FILE_EXECUTIONS = METRICS_FOLDER + PROJECT_NAME + "_exec_figure.pdf"
FIGURE_FILE_TIMESTAMPS = METRICS_FOLDER + PROJECT_NAME + "_tstamps_figure.pdf"
FIGURE_FILE_PERSLICE = METRICS_FOLDER + PROJECT_NAME + "_slice_figure.pdf"
TOTAL_TIME_FILE = PROJECT_NAME + '_total_exec_times.csv'
TOTAL_TIME_FILEPATH = METRICS_FOLDER + PROJECT_NAME + '_total_exec_times.csv'
DURATION_TAG = 'Execution time per slice (ms)'
BILLED_DURATION_TAG = 'Billed duration (ms)'
USED_MEMORY_TAG = 'Max memory used (MB)'
INIT_DURATION_TAG = 'Init duration (ms)'
TOTAL_TIME_TAG = 'Total execution time average (ms)'
CSV_HEADERS_EXECUTIONS = ['Execution number', DURATION_TAG, USED_MEMORY_TAG]
CSV_HEADERS_PERSLICE = ['Execution number', 'Slice', DURATION_TAG, USED_MEMORY_TAG]
CSV_HEADERS_TIMESTAMPS = ['Timestamp (ms)', DURATION_TAG, USED_MEMORY_TAG]
TOTAL_TIME_HEADERS = ['Function', TOTAL_TIME_TAG]
MARKERS = ["+", "x", "1", ".", "*", "^", "<", ">", "v", "s", "p", "o"]



from configparser import ConfigParser


config_parser = ConfigParser()

config_parser.read('../../lambda_code/general_config.ini')
PROJECT_NAME = config_parser.get('project', 'project_name')
NUMBER_OF_SLICES = config_parser.getint('project', 'number_of_slices')

config_parser.read('../sfn_config.ini')
STATE_MACHINE_SUFFIX = config_parser.get('sfn', 'state_machine_suffix')

config_parser.read('../lambda_code/projects/' + PROJECT_NAME + "/" + PROJECT_NAME + "_config.ini")

FUNCTION_NAME = PROJECT_NAME + "_" + str(NUMBER_OF_SLICES) + "_slices"
STATE_MACHINE_NAME = FUNCTION_NAME + "_" + STATE_MACHINE_SUFFIX
EVENT0 = "../../events/event0.json"
STATE_MACHINE_ARN_FILE = "../outputs/state_machine_arn.txt"
EXECUTION_ARN_FILE = "../outputs/execution_arn.txt"

# METRICS
METRICS_FOLDER = "../saved_metrics/" + PROJECT_NAME + "/"
METRICS_FILE = METRICS_FOLDER + FUNCTION_NAME + '_executions.csv'
METRICS_FILE_TIMESTAMPS = METRICS_FOLDER + FUNCTION_NAME + '_timestamps.csv'
TOTAL_TIME_FILE = PROJECT_NAME + '_total_exec_times.csv'
TOTAL_TIME_FILEPATH = METRICS_FOLDER + PROJECT_NAME + '_total_exec_times.csv'
DURATION_TAG = 'Duration (ms)'
BILLED_DURATION_TAG = 'Billed duration (ms)'
USED_MEMORY_TAG = 'Max memory used (MB)'
TOTAL_TIME_TAG = 'Total execution time average (ms)'
CSV_HEADERS = ['Execution', 'Slice', DURATION_TAG, USED_MEMORY_TAG]
CSV_HEADERS_TIMESTAMPS = ['Timestamp (ms)', DURATION_TAG, USED_MEMORY_TAG]
TOTAL_TIME_HEADERS = ['Function', TOTAL_TIME_TAG]
MARKERS = ["x", "+", "1", ".", "*", "o", "v", "s", "p", "^", "<", ">"]



from configparser import ConfigParser

config_parser = ConfigParser()

config_parser.read('../lambda_code/projectname_config.ini')
PROJECT_NAME = config_parser.get('project', 'project_name')

config_parser.read('sfn_config.ini')
STATE_MACHINE_SUFFIX = config_parser.get('sfn', 'state_machine_suffix')

config_parser.read('../lambda_code/projects/' + PROJECT_NAME + "/" + PROJECT_NAME + "_config.ini")

NUMBER_OF_SLICES = config_parser.getint('number_of_slices', 'number_of_slices')

FUNCTION_NAME = PROJECT_NAME + "_" + str(NUMBER_OF_SLICES) + "_slices"
STATE_MACHINE_NAME = FUNCTION_NAME + "_" + STATE_MACHINE_SUFFIX
EVENT0 = "../events/event0.json"
STATE_MACHINE_ARN_FILE="outputs/state_machine_arn.txt"
EXECUTION_ARN_FILE="outputs/execution_arn.txt"

# METRICS
METRICS_FOLDER = "metrics/" + PROJECT_NAME + "/"
METRICS_FILE=METRICS_FOLDER + FUNCTION_NAME + '.csv'
DURATION_TAG = 'Duration (ms)'
BILLED_DURATION_TAG = 'Billed duration (ms)'
USED_MEMORY_TAG = 'Max memory used (MB)'
CSV_HEADERS = ['Lambda function', 'Execution number', DURATION_TAG, BILLED_DURATION_TAG, USED_MEMORY_TAG]


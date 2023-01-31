import sfn_config

import importlib
from lambda_code.src import generic_constants
constants = importlib.import_module(generic_constants.CONSTANTS_MODULE, package=None)


FUNCTION_NAME = constants.PROJECT_NAME + "_" + str(constants.NUMBER_OF_SLICES) + "_slices"
STATE_MACHINE_NAME = FUNCTION_NAME + "_" + sfn_config.STATE_MACHINE_SUFFIX
EVENT0 = "../events/event0.json"
STATE_MACHINE_ARN_FILE="outputs/state_machine_arn.txt"
EXECUTION_ARN_FILE="outputs/execution_arn.txt"



from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read('general_config.ini')

PROJECT_NAME = config_parser.get('project', 'project_name')
NUMBER_OF_SLICES = config_parser.getint('project', 'number_of_slices')

config_parser.read('projects/' + PROJECT_NAME + "/" + PROJECT_NAME + "_config.ini")

ONNX_MODEL = config_parser.get('project', 'onnx_model')
S3_BUCKET = config_parser.get('aws', 's3_bucket')
PREPROCESSED_INPUT = config_parser.get('input', 'preprocessed_input')

parsed_input_list = config_parser.get('project', 'input_list_start')
INPUT_LIST_START = list(parsed_input_list.split("\n"))[1:]

parsed_output_list = config_parser.get('project', 'output_list_end')
OUTPUT_LIST_END = list(parsed_output_list.split("\n"))[1:]

from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read('../lambda_code/general_config.ini')

PROJECT_NAME = config_parser.get('project', 'project_name')
NUMBER_OF_SLICES = config_parser.getint('project', 'number_of_slices')

PACKAGE_FOLDER = "../packages/" + PROJECT_NAME + "/"
PACKAGE_PATH = PACKAGE_FOLDER + PROJECT_NAME + "_" + str(NUMBER_OF_SLICES).zfill(2) + "_slices.zip"

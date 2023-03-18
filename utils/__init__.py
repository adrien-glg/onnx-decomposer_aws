from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read('../lambda_code/general_config.ini')

PROJECT_NAME = config_parser.get('project', 'project_name')

config_parser.read('../lambda_code/projects/' + PROJECT_NAME + "/" + PROJECT_NAME + "_config.ini")

NUMBER_OF_SLICES = config_parser.getint('number_of_slices', 'number_of_slices')

PACKAGE_FOLDER = "../packages/" + PROJECT_NAME + "/"
PACKAGE_PATH = PACKAGE_FOLDER + PROJECT_NAME + "_" + str(NUMBER_OF_SLICES) + "_slices.zip"

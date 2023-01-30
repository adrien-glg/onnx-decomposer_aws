import re
import sfn_constants


def save_to_file(data, filepath):
    with open(filepath, 'w') as outfile:
        outfile.write(str(data))
        outfile.close()


def get_regex_in_file(regex, filepath):
    with open(filepath) as file:
        data = file.read()

    search_result = re.search(regex, data)
    result = str(search_result.group(1))

    return result


def get_state_machine_arn():
    return get_regex_in_file('\'stateMachineArn\': \'(.*)\', \'creationDate\'', sfn_constants.DEPLOYMENT_OUTPUT)


def get_execution_arn():
    return get_regex_in_file('\'executionArn\': \'(.*)\', \'startDate\'', sfn_constants.EXECUTION_OUTPUT)


def get_results():
    return get_regex_in_file('\'output\': \'(.*)\', \'outputDetails\'', sfn_constants.EXECUTION_DESCRIPTION)

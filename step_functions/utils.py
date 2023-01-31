import sfn_constants


def save_to_file(data, filepath):
    with open(filepath, 'w') as outfile:
        outfile.write(str(data))
        outfile.close()


def get_data_from_file(filepath):
    with open(filepath) as file:
        data = file.read()
    return data


def get_state_machine_arn():
    return get_data_from_file(sfn_constants.STATE_MACHINE_ARN_FILE)


def get_execution_arn():
    return get_data_from_file(sfn_constants.EXECUTION_ARN_FILE)

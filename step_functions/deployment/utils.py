from step_functions.deployment import sfn_constants
from datetime import date


def save_to_file(data, filepath):
    with open(filepath, 'w') as outfile:
        outfile.write(str(data))
        outfile.close()


def get_data_from_file(filepath):
    with open(filepath) as file:
        data = file.read()
    return data


def get_state_machine_arn():
    full_arn = get_data_from_file(sfn_constants.STATE_MACHINE_ARN_FILE)
    term = "stateMachine:"
    end_index = full_arn.index(term) + len(term)
    arn_prefix = full_arn[:end_index]
    final_arn = arn_prefix + sfn_constants.STATE_MACHINE_NAME
    return final_arn


def get_execution_arn():
    return get_data_from_file(sfn_constants.EXECUTION_ARN_FILE)


def get_today_date():
    today = date.today()
    today_date = today.strftime("%Y/%m/%d")
    return today_date


def get_duration(message, duration_type="basic"):
    if duration_type == "billed":
        term = 'Billed Duration: '
    elif duration_type == "init":
        term = 'Init Duration: '
    else:
        term = 'Duration: '
    start_index = message.find(term) + len(term)
    end_term = '\t'
    end_index = message[start_index:].find(end_term) + start_index

    duration_with_unit = message[start_index:end_index]
    duration = float(duration_with_unit.split()[0])
    unit = duration_with_unit.split()[1]

    return duration, unit


def get_used_memory(message):
    term = 'Max Memory Used: '
    start_index = message.find(term) + len(term)
    end_term = '\t'
    end_index = message[start_index:].find(end_term) + start_index

    memory_with_unit = message[start_index:end_index]
    memory = int(memory_with_unit.split()[0])
    unit = memory_with_unit.split()[1]

    return memory, unit

import json


def read_json(data):
    """
    data - file name
    """
    with open(data) as json_file:
        data_read = json.load(json_file)

    return data_read

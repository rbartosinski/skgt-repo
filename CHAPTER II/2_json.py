import json


def check_numbers(json_in):

    # Step 1: delete unnecessary/disturbing chars
    list_in = str(json_in)
    for char in ['{', '[', ":", ",", "]", "}"]:
        if char in list_in:
            list_in = list_in.replace(char, " ")

    # Step 2: extracting numbers
    new_list = []
    splitted_list = list_in.split()
    for i in splitted_list:
        if i.isdigit():
            new_list.append(int(i))
        if i.startswith('-'):
            new_list.append(int(i))

    # Step 3: sum it!
    sum_numbers = sum(new_list)
    return sum_numbers


def open_json(name_of_file):

    with open(name_of_file) as js:
        data = json.load(js)
    return data


check_numbers(open_json('skychallenge_accounting_input.txt'))

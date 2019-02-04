def check_single_key(key_to_check, key_line_nr=0):

    splitted_key = key_to_check.split()
    temp_list = []
    temp_join = " "
    for i, name in enumerate(splitted_key):
        if splitted_key[i] not in temp_list:
            temp_list.append(splitted_key[i])
        else:
            print("Warning! Key from line {0} invalid: {1}".format(
                key_line_nr + 1, temp_join.join(splitted_key)))
            break


def check_keys_file(name_of_file):

    file = open_file(name_of_file)
    for line, key in enumerate(file):
        check_single_key(key, line)


def open_file(name_of_file):

    with open(name_of_file) as file:
        data = file.read().splitlines()
    return data


check_single_key("aa bb cc dd aa")
check_keys_file('skychallenge_skyphrase_input.txt')

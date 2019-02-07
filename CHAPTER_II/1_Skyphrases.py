def check_keys_file(name_of_file):

    # open required file using separate function
    file = open_file(name_of_file)

    # define keys counter and list of invalid keys
    all_keys_counter = 0
    invalid_keys_list = []

    # checking each line key by sending it to validator
    for line, key in enumerate(file):
        all_keys_counter += 1
        invalid_key = key_validator(key)

        # append invalid key to list
        if invalid_key is True:
            invalid_keys_list.append(key)

    # finally, find number of good keys
    number_of_validated_keys = all_keys_counter - len(invalid_keys_list)
    return number_of_validated_keys


def key_validator(key_to_check):

    # splitting each key to checking and comparing phrases
    splitted_key = key_to_check.split()
    phrase_temp_list = []
    for i, name in enumerate(splitted_key):
        if splitted_key[i] not in phrase_temp_list:
            phrase_temp_list.append(splitted_key[i])
        else:
            return True
    return False


def open_file(name_of_file):

    with open(name_of_file) as file:
        data = file.read().splitlines()
    return data


check_keys_file('skychallenge_skyphrase_input.txt')

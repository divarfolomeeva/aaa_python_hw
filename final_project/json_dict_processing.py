def extract_nested_value(obj, keys):
    current = obj

    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        elif isinstance(current, list):
            try:
                index = int(key)
                current = current[index]
            except (ValueError, IndexError):
                return None
        else:
            return None

        if current is None:
            return None

    return current


def process_dictionary_with_config(dictionary, config):
    result = {}

    for attribute, path_info in config.items():
        if isinstance(path_info, tuple):
            path, process_func = path_info
            raw_value = extract_nested_value(dictionary, path)

            if raw_value is not None:
                result[attribute] = process_func(raw_value)
            else:
                result[attribute] = None
        else:
            path = path_info
            result[attribute] = extract_nested_value(dictionary, path)

    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    result = []

    for dictionary in list_of_dicts:
        processed = process_dictionary_with_config(dictionary, config)
        result.append(processed)

    return result


def create_processor(config, list_processor=False):
    if list_processor:
        def processor(list_of_dicts):
            return process_list_of_dicts_with_config(list_of_dicts, config)
    else:
        def processor(dictionary):
            return process_dictionary_with_config(dictionary, config)

    return processor
"""
Functions for converting a cookiecutter.json file to a piecutter_config.py file.
"""


def config_dict(name, prompt_type):
    return {'name': name, 'prompt_type': prompt_type}


def cookiecutter_dict_to_piecutter_list(cookiecutter_dict):
    """
    Given a dictionary of cookiecutter.json keys and values, return a list of
    dictionaries for piecutter_config.py.
    """
    piecutter_list = []
    for key, val in cookiecutter_dict.items():
        if key.startswith(u'_'):
            dict_ = config_dict(key, 'raw')
            dict_['value'] = val
            piecutter_list.append(dict_)
        elif isinstance(val, list):
            dict_ = config_dict(key, 'choice')
            dict_['choices'] = val
            dict_['default_value'] = val[0]
            piecutter_list.append(dict_)
        elif isinstance(val, str):
            dict_ = config_dict(key, 'text')
            dict_['default_value'] = val
            piecutter_list.append(dict_)
        elif isinstance(val, dict):
            pass # raise exception
        else:
            pass # raise exception
    return piecutter_list

from piecutter.convert import cookiecutter_dict_to_piecutter_list


def test_cookiecutter_dict_to_piecutter_list():
    cookiecutter_dict = {
        'text_var': 'this is a string',
        'list_var': ['foo', 'bar'],
        '_extensions': ['jinja2_time.TimeExtension'],
    }
    piecutter_list = cookiecutter_dict_to_piecutter_list(cookiecutter_dict)
    expected_list = [
        {'name': 'text_var', 'prompt_type': 'text', 'default_value': 'this is a string'},
        {'name': 'list_var', 'prompt_type': 'choice', 'choices': ['foo', 'bar'], 'default_value': 'foo'},
        {'name': '_extensions', 'prompt_type': 'raw', 'value': ['jinja2_time.TimeExtension']},
    ]
    assert piecutter_list == expected_list

 # TODO add test that dictionary value raises an exception

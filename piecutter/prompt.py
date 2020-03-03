"""Functions for prompting the user for project info."""

from collections import OrderedDict

import click


def read_user_variable(var_name, default_value):
    """Prompt user for variable and return the entered value or given default.
    :param str var_name: Variable of the context to query the user
    :param default_value: Value that will be returned if no input happens
    """
    # Please see http://click.pocoo.org/4/api/#click.prompt
    return click.prompt(var_name, default=default_value)


def read_user_choice(var_name, choices, default_value):
    """Prompt the user to choose from several options for the given variable.
    :param str var_name: Variable as specified in the context
    :param list choices: Sequence of options that are available to select from
    :param str default_value: The default choice (this should be one of the strings in ``choices``)
    :return: Exactly one item of ``choices`` that has been chosen by the user
    """
    choice_map = OrderedDict(
        (u'{}'.format(i), value) for i, value in enumerate(choices, 1)
    )
    choices = choice_map.keys()

    choice_lines = []
    default = u'1'
    for choice_index, choice_value in choice_map.items():
        choice_lines.append(f'{choice_index} - {choice_value}')
        if choice_value == default_value:
            default = f'{choice_index}'

    prompt = u'\n'.join((
        u'Select {}:'.format(var_name),
        u'\n'.join(choice_lines),
        u'Choose from {}'.format(u', '.join(choices))
    ))

    user_choice = click.prompt(
        prompt, type=click.Choice(choices), default=default, show_choices=False
    )
    return choice_map[user_choice]


def prompt_user_for_config(prompt_config, no_input=False):
    """
    """
    cookiecutter_dict = OrderedDict([])

    # First pass: Handle text and raw variables, plus choices.
    # These must be done first because the dictionaries keys and
    # values might refer to them.
    # TODO handle the use of jinja template variables within the config itself
    for prompt_item in prompt_config:
        var_name = prompt_item['name']
        prompt_type = prompt_item['prompt_type']
        if prompt_type == 'raw':
            cookiecutter_dict[var_name] = prompt_item['value']
        elif prompt_type == 'text':
            val = prompt_item['default_value']
            if not no_input:
                val = read_user_variable(var_name, val)
            cookiecutter_dict[var_name] = val
        elif prompt_type == 'choice':
            val = prompt_item['default_value']
            if not no_input:
                val = read_user_choice(var_name, prompt_item['choices'], val)
            cookiecutter_dict[var_name] = val
    # TODO Second pass; handle the dictionaries.

    return cookiecutter_dict

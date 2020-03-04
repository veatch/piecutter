import importlib
import logging
import os
from collections import OrderedDict

from cookiecutter.config import get_user_config
from cookiecutter.generate import generate_files
from cookiecutter.utils import rmtree

from piecutter import constants
from piecutter.prompt import prompt_user_for_config
from piecutter.repository import determine_repo_dir

logger = logging.getLogger(__name__)


def piecutter(template, checkout=None, no_input=False, overwrite_if_exists=False,
        output_dir='.', user_config_file=None, default_config=False):
    """
    :param template: A directory containing a project template directory,
        or a URL to a git repository.
    :param checkout: The branch, tag or commit ID to checkout after clone.
    :param no_input: Prompt the user at command line for manual configuration?
    :param: overwrite_if_exists: Overwrite the contents of output directory
        if it exists.
    :param output_dir: Where to output the generated project dir.
    :param user_config_file: User configuration file path.
    :param default_config: Use default values rather than a config file.
    """
    config_dict = get_user_config(
        config_file=user_config_file,
        default_config=default_config,
    )

    repo_dir, cleanup = determine_repo_dir(
        template=template,
        abbreviations=config_dict['abbreviations'],
        clone_to_dir=config_dict['cookiecutters_dir'],
        checkout=checkout,
        no_input=no_input,
    )

    template_name = os.path.basename(os.path.abspath(repo_dir))

    prompt_config_file = os.path.join(repo_dir, constants.PROMPT_CONFIG_FILE)
    msg = u'prompt_config_file is %s, loading module and calling prompt_config function'
    logger.debug(msg, prompt_config_file)
    spec = importlib.util.spec_from_file_location('cookiecutter_config', prompt_config_file)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)
    prompt_config = config_module.prompt_config()
    # TODO add some validation here that each item has needed fields, a valid prompt_type, etc

    template_context = OrderedDict([])
    template_context['cookiecutter'] = prompt_user_for_config(prompt_config, no_input)
    # TODO add template dir or url to template_context['_template'] and dump
    # template_context to replay_dir
    # TODO write to .piecutter.json file (or something) before generating files
    result = generate_files(
        repo_dir=repo_dir,
        context=template_context,
        overwrite_if_exists=overwrite_if_exists,
        output_dir=output_dir
    )

    # Cleanup (if required)
    if cleanup:
        rmtree(repo_dir)

    return result

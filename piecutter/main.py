import importlib
import logging
import os

from cookiecutter.config import get_user_config
from cookiecutter.repository import determine_repo_dir

logger = logging.getLogger(__name__)
PROMPT_CONFIG_FILE = 'cookiecutter_config.py'


def piecutter(template, checkout=None, no_input=False, user_config_file=None,
        default_config=False):
    """
    :param template: A directory containing a project template directory,
        or a URL to a git repository.
    :param checkout: The branch, tag or commit ID to checkout after clone.
    :param no_input: Prompt the user at command line for manual configuration?
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

    prompt_config_file = os.path.join(repo_dir, PROMPT_CONFIG_FILE)
    logger.debug(f'prompt_config_file is {prompt_config_file}')
    spec = importlib.util.spec_from_file_location('cookiecutter_config', prompt_config_file)
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)
    prompt_config = config_module.prompt_config()
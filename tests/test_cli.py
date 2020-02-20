import os

import pytest
from click.testing import CliRunner
from cookiecutter import utils

from piecutter.__main__ import main


@pytest.fixture(scope='session')
def cli_runner():
    """Fixture that returns a helper function to run the cookiecutter cli."""
    runner = CliRunner()

    def cli_main(*cli_args):
        """Run cookiecutter cli main with the given args."""
        return runner.invoke(main, cli_args)

    return cli_main

@pytest.fixture
def remove_fake_project_dir(request):
    """Remove the fake project directory created during the tests."""
    def fin_remove_fake_project_dir():
        if os.path.isdir('fake-project'):
            utils.rmtree('fake-project')
    request.addfinalizer(fin_remove_fake_project_dir)

@pytest.mark.usefixtures('remove_fake_project_dir')
def test_cli(cli_runner):
    result = cli_runner('tests/fake-repo-pre/', '--no-input')
    assert result.exit_code == 0
    #assert os.path.isdir('fake-project')
    #with open(os.path.join('fake-project', 'README.rst')) as f:
        #assert 'Project name: **Fake Project**' in f.read()

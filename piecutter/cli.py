import click

from piecutter.main import piecutter


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.argument(u'template')
@click.option(
    u'--no-input', is_flag=True,
    help=u'Do not prompt for parameters and only use cookiecutter.json '
         u'file content',
)
@click.option(
    u'-c', u'--checkout',
    help=u'branch, tag or commit to checkout after git clone',
)
@click.option(
    u'--config-file', type=click.Path(), default=None,
    help=u'User configuration file'
)
@click.option(
    u'--default-config', is_flag=True,
    help=u'Do not load a config file. Use the defaults instead'
)
def main(template, no_input, checkout, config_file, default_config):
    piecutter(
        template, checkout, no_input,
        user_config_file=config_file,
        default_config=default_config,
    )

import click

from piecutter.main import piecutter


@click.command(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.argument(u'template')
def main(template):
    piecutter(template)

from click_repl import repl
import click
from .util import get_help_info


@click.command("shell")
def shell():
    click.echo(":q to quit; :h to get help; --help to get commands")
    repl(click.get_current_context())


@click.command('help')
@click.option('--display', is_flag=True, help='show cmd structure in console')
@click.pass_context
def help(ctx, display):
    """Generate cmd structure json and get help info"""
    # get parent object
    root = click.get_current_context().__dict__['parent'].__dict__['command']
    get_help_info(root, display=display)
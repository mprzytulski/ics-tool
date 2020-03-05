import click

from ics_tool.merge import merge


@click.group()
def cli():
    """
    Internet Calendaring and Scheduling (ics) file manipulation tool
    """
    pass


cli.add_command(merge)

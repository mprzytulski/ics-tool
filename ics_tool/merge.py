import re
from os.path import isfile

import click
import requests
from click import UsageError
from ics import Calendar


def read_ics(source: str):
    if re.match("https?://", source):
        return requests.get(source).text
    elif isfile(source):
        with open(source) as f:
            return f.read()

    raise UsageError(f"Unable to fetch source {source}")


@click.command()
@click.option("--creator", "-c", help="Calendar creator", default="ics-tool")
@click.option("--output", "-o", help="Output format", type=click.File('w+'), default="-")
@click.argument("sources", nargs=-1)
def merge(sources, output, creator):
    """
    Merge multiple ics files into one
    """
    merged = Calendar(creator=creator)

    for source in sources:
        calendar = Calendar(read_ics(source))

        for event in calendar.events:
            merged.events.add(event)

    output.write(str(merged))

import rich_click as click
import os


@click.group("", help="The entrypoint for the command-line application.")
@click.option("--dry-run",
              help="No transactions are performed. A list of files that would have been converted are instead "
                   "displayed.")
@click.option("--log-level", type=click.Choice(["INFO", "DEBUG", "WARN", "FATAL", "ERROR"]),
              help="The logging verbosity to use.")
def cli():
    return

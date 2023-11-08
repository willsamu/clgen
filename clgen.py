# clgen.py
import click
from config import configure_profile


@click.group()
def clgen():
    """Cover Letter Generator CLI."""
    pass


@clgen.command()
def configure():
    """Configure user profile."""
    configure_profile()


if __name__ == "__main__":
    clgen()

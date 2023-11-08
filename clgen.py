# clgen.py
import click
from config import configure_profile, add_cv, delete_cv, display_cv


@click.group()
def clgen():
    """Cover Letter Generator CLI."""
    pass


@clgen.command()
def configure():
    """Configure user profile."""
    configure_profile()


@clgen.command()
def cv_add():
    """Add a new CV."""
    add_cv()


@clgen.command()
def cv_delete():
    """Delete an existing CV."""
    delete_cv()


@clgen.command()
def cv_display():
    """Display an existing CV."""
    display_cv()


if __name__ == "__main__":
    clgen()

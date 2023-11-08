# config.py
from dotenv import load_dotenv, set_key
import click
import os


def configure_profile():
    # Load existing .env file or create one if it doesn't exist
    load_dotenv(".env")

    # Check if a profile already exists
    if os.getenv("FULL_NAME"):
        if click.confirm("Profile already exists. Update?"):
            _ask_and_set_config()
        else:
            click.echo("Configuration unchanged.")
    else:
        _ask_and_set_config()


def _ask_and_set_config():
    # Ask for user input
    full_name = click.prompt("Enter your full name")
    street = click.prompt("Enter your street")
    street_number = click.prompt("Enter your street number")
    zip_code = click.prompt("Enter your zip")
    city = click.prompt("Enter your city")
    country = click.prompt("Enter your country")

    # Persist configuration
    set_key(".env", "FULL_NAME", full_name)
    set_key(".env", "STREET", street)
    set_key(".env", "STREET_NUMBER", street_number)
    set_key(".env", "ZIP", zip_code)
    set_key(".env", "CITY", city)
    set_key(".env", "COUNTRY", country)

    click.echo("Configuration saved.")


def add_cv():
    cv_name = click.prompt("Enter the name for the CV")
    cv_content = click.edit("Enter the CV content (multiline supported):")
    if cv_content:
        cv_path = f"cvs/{cv_name}.txt"
        with open(cv_path, "w") as cv_file:
            cv_file.write(cv_content)
        click.echo(f'CV "{cv_name}" saved.')


def delete_cv():
    cvs = _get_cv_list()
    if cvs:
        for idx, cv in enumerate(cvs, start=1):
            click.echo(f"{idx}. {cv}")
        cv_index = click.prompt("Enter the number of the CV to delete", type=int)
        if 0 < cv_index <= len(cvs):
            os.remove(f"cvs/{cvs[cv_index - 1]}")
            click.echo(f'CV "{cvs[cv_index - 1]}" deleted.')
        else:
            click.echo("Invalid CV number.")
    else:
        click.echo("No CVs found.")


def display_cv():
    cvs = _get_cv_list()
    if cvs:
        for idx, cv in enumerate(cvs, start=1):
            click.echo(f"{idx}. {cv}")
        cv_index = click.prompt("Enter the number of the CV to display", type=int)
        if 0 < cv_index <= len(cvs):
            cv_path = f"cvs/{cvs[cv_index - 1]}"
            with open(cv_path, "r") as cv_file:
                click.echo(cv_file.read())
        else:
            click.echo("Invalid CV number.")
    else:
        click.echo("No CVs found.")


def _get_cv_list():
    return [cv for cv in os.listdir("cvs") if cv.endswith(".txt")]


# Make sure the cvs directory exists
os.makedirs("cvs", exist_ok=True)

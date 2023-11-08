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

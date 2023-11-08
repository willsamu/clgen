# setup.py
from setuptools import setup, find_packages

packages = find_packages()
print(packages)

setup(
    name="clgen",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "python-dotenv",
        "requests",
        "markdown",
        "openai",
        # Add other dependencies you might have
    ],
    entry_points="""
        [console_scripts]
        clgen=clgen.clgen:clgen
    """,
)

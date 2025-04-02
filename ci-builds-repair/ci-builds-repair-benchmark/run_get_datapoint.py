import json
import ruamel.yaml
import click
import os
import sys
from types import SimpleNamespace
from benhmark_functions import get_datapoint

def load_config():
    yaml = ruamel.yaml.YAML(typ='rt')
    with open("config.yaml", "r") as file:
        return yaml.load(file)

@click.command()
@click.option('--json_input', type=str, required=True, help="JSON string input")
@click.option('--model_name', type=str, required=True, help="model name")
def process_json(json_input, model_name):
    try:
        datapoint = json.loads(json_input)
    except json.JSONDecodeError:
        click.echo("Invalid JSON input", err=True)
        sys.exit(1)
    
    
    try:
        config = SimpleNamespace(**load_config())
        credentials = {
            "username": config.username_gh,
           "token": config.token_gh,
            "model": model_name,
        }
        repo, user_branch_name = get_datapoint(datapoint, config, credentials)
        click.echo(user_branch_name)
        sys.exit(0)
    except Exception as e:
        click.echo(f"An unexpected error occurred: {str(e)}" , err=True)
        click.echo(f"An unexpected error occurred:\n{traceback.format_exc()}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    process_json()

import json
import ruamel.yaml
import click
from benhmark_functions import get_datapoint

def load_config():
    with open("config.yaml", "r") as file:
        return ruamel.yaml.load(file)

@click.command()
@click.argument('json_input', type=click.STRING)
def process_json(json_input):
    try:
        datapoint = json.loads(json_input)
    except json.JSONDecodeError:
        click.echo("Invalid JSON input", err=True)
        return "Invalid JSON"
    
    config = load_config()
    
    try:
        self.credentials = {
            "username": self.config.username_gh,
            "token": os.environ.get("TOKEN_GH"),
            "model": model_name,
        }
        result = get_datapoint(datapoint, config, credentials)
        return 0
    except Exception as e:
        click.echo(f"An unexpected error occurred: {str(e)}" , err=True)
        return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    process_json()

import json
import ruemal.yaml
import click
from benchmark_functions import get_datapoint

def load_config():
    with open("config.yaml", "r") as file:
        return ruemal.yaml.load(file)

@click.command()
@click.argument('json_input', type=click.STRING)
def process_json(json_input):
    try:
        datapoint = json.loads(json_input)
    except json.JSONDecodeError:
        click.echo("Invalid JSON input", err=True)
        return
    
    config = load_config()
    
    self.credentials = {
        "username": self.config.username_gh,
        "token": os.environ.get("TOKEN_GH"),
        "model": model_name,
    }
    result = get_datapoint(datapoint, config, credentials)
    click.echo(json.dumps(result, indent=2))

if __name__ == "__main__":
    process_json()

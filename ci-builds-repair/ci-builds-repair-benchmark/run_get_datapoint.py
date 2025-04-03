import click
import os
import sys
import traceback
import scripts_utils
from datasets import load_dataset
from types import SimpleNamespace
from benhmark_functions import get_datapoint


@click.command()
@click.option('--id', 'data_id', required=True, type=str, help='ID of the data point to fetch')
@click.option('--model_name', type=str, required=True, help="model name")
def process_json(data_id, model_name):
    try:
        datapoint = scripts_utils.fetch_datapoint(data_id)
        config = SimpleNamespace(**scripts_utils.load_config())
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

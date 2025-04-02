import json
import ruamel.yaml
import click
import git
import os
from types import SimpleNamespace
from benhmark_functions import push_repo
import traceback

def load_config():
    yaml = ruamel.yaml.YAML(typ='rt')
    with open("config.yaml", "r") as file:
        return yaml.load(file)

@click.command()
@click.option('--repo_path', type=str, required=True, help="Path to the fixed repo.")
@click.option('--model_name', type=str, required=True, help="model name")
@click.option('--user_branch_name', type=str, required=True, help="user branch name provided by run_get_datapoint")
@click.option('--repo_name', type=str, required=True, help="repo name in instace datapoint")
@click.option('--repo_owner', type=str, required=True, help="repo owner in instance datapoint")
@click.option('--json_input', type=str, required=True, help="JSON string input")
def process_json(repo_path, model_name, user_branch_name, repo_name, repo_owner, json_input ):
    try:
        datapoint = json.loads(json_input)
    except json.JSONDecodeError:
        click.echo("Invalid JSON input", err=True)
        return "Invalid JSON"
    try:
        config = SimpleNamespace(**load_config())
        config.user_branch_name = user_branch_name
        repo = git.Repo(repo_path)
        repo.name, repo.owner = repo_name, repo_owner
        credentials = {
            "username": config.username_gh,
            "token": os.environ.get("TOKEN_GH"),
            "model": model_name,
        }
        benchmark_owner = config.benchmark_owner
        user_branch_name = config.user_branch_name
        commit_sha  = push_repo(repo, credentials, benchmark_owner, user_branch_name)
        job_identificator = {
            "repo_name": repo.name,
            "commit": commit_sha,
            "id": datapoint["id"],
            "sha_original": datapoint["sha_fail"],
            "branch_name": user_branch_name,
            "difficulty": datapoint["difficulty"],
        }
        click.echo(result)
        return 0
    except Exception as e:
        click.echo(f"An unexpected error occurred: {str(e)}" , err=True)
        click.echo(f"An unexpected error occurred:\n{traceback.format_exc()}", err=True)

        return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    process_json()


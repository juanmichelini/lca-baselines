import json
import click
import git
import sys
import os
import scripts_utils
from types import SimpleNamespace
from benhmark_functions import push_repo
import traceback

@click.command()
@click.option('--model-name', type=str, required=True, help="model name")
@click.option('--user-branch-name', type=str, required=True, help="user branch name provided by run_get_datapoint")
@click.option('--id', 'data_id', required=True, type=str, help='ID of the data point to fetch')
def process_json(model_name, user_branch_name, data_id ):
    try:
        datapoint = scripts_utils.fetch_datapoint(data_id)
        config = SimpleNamespace(**scripts_utils.load_config())
        config.user_branch_name = user_branch_name
        repo_path = os.path.join(config.repos_folder, f"{datapoint['repo_owner']}__{datapoint['repo_name']}")
        repo = git.Repo(repo_path)
        repo.name, repo.owner = datapoint['repo_name'], datapoint['repo_owner']
        credentials = {
            "username": config.username_gh,
            "token": config.token_gh,
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
        click.echo(json.dumps(job_identificator, indent=2))
        sys.exit(0)
    except Exception as e:
        click.echo(f"An unexpected error occurred: {str(e)}" , err=True)
        click.echo(f"An unexpected error occurred:\n{traceback.format_exc()}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    process_json()


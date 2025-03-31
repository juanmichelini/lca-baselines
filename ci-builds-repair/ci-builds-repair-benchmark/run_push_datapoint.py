import json
import ruamel.yaml
import click
import git
from benhmark_functions import push_repo

def load_config():
    with open("config.yaml", "r") as file:
        return ruamel.yaml.load(file)

@click.command()
@click.argument('repo_path', type=click.STRING)
def process_json(json_input):
    try:
        config = load_config()
        repo = git.Repo(repo_path)
        self.credentials = {
            "username": self.config.username_gh,
            "token": os.environ.get("TOKEN_GH"),
            "model": model_name,
        }
        benchmark_owner = config.benchmark_owner
        user_branch_name = config.user_branch_name
        result = push_repo(repo, credentials, benchmark_owner, user_branch_name)
        return 0
    except Exception as e:
        click.echo(f"An unexpected error occurred: {str(e)}" , err=True)
        return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    process_json()


import json
import ruemal.yaml
import click
import git
from benchmark_functions import push_repo

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

@click.command()
@click.argument('repo_path', type=click.STRING)
def process_json(json_input):
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
    click.echo(json.dumps(result, indent=2))

if __name__ == "__main__":
    process_json()


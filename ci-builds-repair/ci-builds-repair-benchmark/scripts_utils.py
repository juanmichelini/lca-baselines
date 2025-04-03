from datasets import load_dataset
import ruamel.yaml

def load_config():
    yaml = ruamel.yaml.YAML(typ='rt')
    with open("config.yaml", "r") as file:
        return yaml.load(file)

def fetch_datapoint(data_id):
    dataset = load_dataset("JetBrains-Research/lca-ci-builds-repair", split="test").to_pandas()
    try:
        data_id = float(data_id)  # Convert to float or int if applicable
    except ValueError:
        print(f"Invalid data_id value: {data_id} cannot be converted to a number.")
        return None
    row = dataset[dataset["id"] == data_id]
    
    if not row.empty:
        return row.iloc[0].to_dict()  # Convert the first matching row to a dictionary
    return None

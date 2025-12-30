from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True

def load_yaml(path: str):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.load(file)
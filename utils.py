import yaml
from munch import munchify

def load_yaml(filepath):
    """
    Loads a yaml file as a Munch object (dictionary of dictionaries).
    
    Args:
        filepath (str): The filepath of the YAML file.
    
    Returns:
        out (dict): A dictionary of dictionaries representing the contents of the YAML file.
    """
    with open(filepath, 'r') as file:
        out = yaml.safe_load(file)
        out = munchify(out)
    return out
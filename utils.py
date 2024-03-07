import yaml
from munch import munchify

def load_sura():
    filepath = './sura.yml'
    with open(filepath, 'r') as file:
        sura = yaml.safe_load(file)
        sura = munchify(sura)
    return sura
import yaml

def read(path):
  with open(path, 'r') as fl:
      return yaml.safe_load(fl)
import yaml


def loadfile(filename):
    with open(filename, 'r') as stream:
        return yaml.load(stream, Loader=yaml.FullLoader)

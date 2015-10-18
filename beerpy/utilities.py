import os


DATA_DIR = "data"


def datadir():
    import beerpy
    pkg_dir = os.path.dirname(beerpy.__file__)
    return os.path.join(pkg_dir, DATA_DIR)

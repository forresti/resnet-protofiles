import os

def mkdir_p(path):
    if not os.access(path, os.F_OK):
        os.mkdir(path)


# **glob —** Search for files using wildcards
from glob import glob

files = glob("files/*.csv")

for file in files:
    print(f"Found file: {file}")
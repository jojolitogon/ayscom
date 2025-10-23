# **open() —** Read/write local files:

with open("../files/data.txt", "r") as f:
    content = f.read()
    print(content)
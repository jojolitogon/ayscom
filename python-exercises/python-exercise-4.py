# **os —** Work with files and folders
import os

# Create folder
os.mkdir("data")

with open("data/new.txt", "w") as file:
    file.write("Using os module")

# Rename             
os.rename("data/new.txt", "data/changed.txt")
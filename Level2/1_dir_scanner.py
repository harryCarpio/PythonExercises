# Write a Python program to scan a specified directory and identify the sub directories and files.
import os

path = 'C:/Users/harry/Videos'

print("Directory: {}".format(path))
for root, directories, files in os.walk(path, topdown=True):
    for name in files:
        print("{} [file]".format(os.path.join(root, name)))
    for name in directories:
        print("{} [sub-directory]".format(os.path.join(root, name)))

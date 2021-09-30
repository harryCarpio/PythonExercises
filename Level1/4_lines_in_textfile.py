# Write a Python program to count the number of lines in a text file.
import os

filepath = "res/textfile2.txt"
absolute_filepath = os.path.dirname(__file__) + os.sep + filepath

file = open(absolute_filepath, "r")

line_count = 0

for line in file:
    line_count += 1
file.close()

print("File {0} has {1} lines".format(filepath, line_count))

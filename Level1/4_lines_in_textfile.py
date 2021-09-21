#Write a Python program to count the number of lines in a text file.

filepath="res/textfile2.txt"
file = open(filepath, "r")

line_count = 0

for line in file:
    line_count += 1
file.close()

print("File {0} has {1} lines".format(filepath, line_count))
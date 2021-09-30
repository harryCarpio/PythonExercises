# Write a Python program to count the frequency of words in a text file
import re
import os

filepath = "res/moby_dick.txt"
absolute_filepath = os.path.dirname(__file__) + os.sep + filepath

file = open(absolute_filepath, "r")

punctuation_signs = [',', '.', '!', '?', '-', ':', ';']

words_count = {}

for line in file:
    line = re.sub(r'[^\w]', ' ', line)
    for word in line.split():
        if words_count.__contains__(word):
            words_count[word] = words_count[word] + 1
        else:
            words_count[word] = 1

file.close()

for word in words_count:
    print("{0}: {1}".format(word, words_count[word]))

"""Write a Python program that reads a JSON object from a file, sorts the object keys in ascending order, then writes
the JSON object back into the file. """
# This version just consider the first level keys for sorting
import json
import os

filepath = "res/src_example_1.json"
output_filepath = "res/sorted_example_1.json"

abs_filepath = os.path.dirname(__file__) + os.sep + filepath
abs_output_filepath = os.path.dirname(__file__) + os.sep + output_filepath

json_file = open(abs_filepath, "r")

data = json.load(json_file)
keys = data.keys()
sorted_keys = sorted(keys)

json_out = {}
for key in sorted_keys:
    json_out[key] = data[key]

with open(abs_output_filepath, "w") as outfile:
    json.dump(json_out, outfile)

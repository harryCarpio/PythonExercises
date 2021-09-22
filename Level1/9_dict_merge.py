# Write a Python function to merge two dictionaries.
def merge_dict(dict1, dict2):
    merged_dict = dict1 | dict2
    return merged_dict


dict1 = {'a': 10, 'b': 8, 'd': 10}
dict2 = {'e': 6, 'c': 4, 'd': 4}

print("Dict 1: {0}".format(dict1))
print("Dict 2: {0}".format(dict2))
print("Merged dict: {0}".format(merge_dict(dict1, dict2)))

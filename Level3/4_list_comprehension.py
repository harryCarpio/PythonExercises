"""
Write a Python function using list comprehension that receives a list of words and returns a list that contains:
The number of characters in each word if the word has 3 or more characters
The string “x” if the word has fewer than 3 characters
"""


def list_comprehension(a_list):
    result_list = []
    for element in a_list:
        if len(element) >= 3:
            result_list.append(len(element))
        else:
            result_list.append("x")
    return result_list


my_list = ['May', 'the', 'Force', 'be', 'with', 'you']
print(list_comprehension(my_list))

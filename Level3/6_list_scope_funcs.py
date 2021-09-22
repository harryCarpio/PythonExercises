"""Write a python file with two functions: a function that receives a number and appends to a global variable list,
and another function that returns this list ordered. """
a_list = [2, 7, 4]


def append_number(a_number):
    global a_list
    a_list.append(a_number)


def ordered_list():
    return sorted(a_list)


print("Original global list:", a_list)
append_number(1)
print("Global list after appends 1:", a_list)
print("Returned ordered list:", ordered_list())
print("Final global list:", a_list)

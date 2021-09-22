'''
Create a Python function that accepts any number of positional and keyword arguments, and that prints them back to the
user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword
arguments.
'''


def arguments_identificator(*args, **kwargs):
    for arg in args:
        print(arg, " provided as positional argument")

    for key, value in kwargs.items():
        print("{0}={1} provided as keyword argument".format(key,value))


arguments_identificator(3, [2, 'aa'], 44, None, p1="ggg")

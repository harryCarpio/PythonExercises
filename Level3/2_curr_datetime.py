"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
import time

current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print("Current date and time:\n{}".format(current_time))

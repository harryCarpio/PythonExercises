'''
Write a Python program that accepts a filename from the user and prints the filename’s extension.
Sample filename : abc.java
Output : java
'''

filename = input("Enter a filename (include extension): ")

if filename.__contains__("."):
    print(filename.split(".")[1])
else:
    print("Write a filename in a proper format, please")
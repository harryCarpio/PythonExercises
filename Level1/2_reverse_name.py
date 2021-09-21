#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

firstname = input("Enter a Firstname: ")
lastname = input("Enter a Lastname: ")

print("{0} {1}".format(lastname, firstname))
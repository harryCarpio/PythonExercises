# Write a Python function to remove duplicates from a list.

def remove_duplicates(a_list):
    return list(dict.fromkeys(a_list))


pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938"
pi_digits = list(pi)

print("Original list:")
print(pi_digits)

print("List with no duplicates:")
print(remove_duplicates(pi_digits))

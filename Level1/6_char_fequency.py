'''
Write a Python program that takes an input string from the user and counts the frequency of characters in the string.
Sample String : google.com
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''

text = input("Enter a text: ")

char_count = {}

for char in text:
    if char_count.__contains__(char):
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1

print(char_count)

#Write a Python program to test whether a passed letter is a vowel or not.

letter = input("Enter a letter: ")

if letter.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(letter, "is a Vowel")
else:
    print(letter, "is not a Vowel")
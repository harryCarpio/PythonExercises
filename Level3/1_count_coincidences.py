"""Write a Python program to count the number of strings where the string length is 2 or more and the first and last
character are the same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2 """

list_string = ['abc', 'xyz', 'aba', '1221', '10']

counter = 0
for s in list_string:
    if len(s) >= 2 and s[0] == s[-1]:
        counter += 1

print(counter)

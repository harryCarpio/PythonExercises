list_string = ['abc', 'xyz', 'aba', '1221', '10']

counter = 0
for s in list_string:
    if(len(s)>=2 and s[0]==s[-1]):
        counter += 1

print(counter)
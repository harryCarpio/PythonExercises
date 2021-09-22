'''
Write a Python program that iterates through integers from 1 to 100 and prints them.
For integers that are multiples of three, print "Fizz" instead of the number.
For integers that are multiples of five, print "Buzz".
For integers which are multiples of both three and five print, "FizzBuzz".
'''

for i in range(100):
    if (i+1) % 3 == 0 and (i+1) % 5 != 0:
        print('Fizz')
    elif (i+1) % 5 == 0 and (i+1) % 3 != 0:
        print('Buzz')
    elif (i+1) % 3 == 0 and (i+1) % 5 == 0:
        print('FizzBuzz')
    else:
        print(i + 1)

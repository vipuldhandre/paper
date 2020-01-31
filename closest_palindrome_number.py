##def palindrome(num):
##    if str(num) == str(num)[::-1]:
##        print("Palindrome")
##    else:
##        print("Not")
##
##palindrome(2002)

num = int(input("Enter a number:"))
def Previous_Palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x
previous = Previous_Palindrome(num)
 
import sys
def next_palindrome(num):
    for x in range(num+1,sys.maxsize):
        if str(x) == str(x)[::-1]:
            return x
next_element = next_palindrome(num)

if (num - previous) < (next_element - num):
    print("Closest palindome is:",previous)

elif(num - previous) == (next_element - num):
    print("Both are closest.And, numbers are:",previous,next_element)
    
else:
    print("Closest palindrome is:",next_element)

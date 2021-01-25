"""Here e have to find the smallest number and the second smallest number
from the input of 10 numbers.

"""
s1 = 0
s2 = 0


for i in range(10):
    n = int(input("Enter a number: "))
    if i == 0:
        s1 = n
    elif i == 1:
        s2 = s1
        s1 = n
    else:
        if n <= s1:
            s1 = n
            s2 = s1
        elif n <= s2:
            s1 = n
            s2 = s2
        else:
            s1 = s1
            s2 = s2
print("the smallest number is: ",s1)
print("the second smallest number is: ",s2)


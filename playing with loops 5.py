"""here we have to find the value of the series
s = 1+x+x^2+x^3+...x^n

ok,lets start
"""
# for this we will a math package or library.
import math as m
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
s = 1
for i in range(1,n+1):
    s = int(s + m.pow(x,i))
    print(s)
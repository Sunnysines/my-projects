n = int(input("enter any three digit number: "))
s = 0
while n > 0:
    r = n % 10
    n = n//10
    s = s * 10 + r
print("reverse number: ", s)

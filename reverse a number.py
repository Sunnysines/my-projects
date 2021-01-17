"""we have to reverse a number which is greater than 1000"""
num = int(input("enter a number greater than 1000: "))
reversed_num = 0
n = num
if num > 1000:

    while n > 0:
        r = n % 10
        n = n//10
        reversed_num = reversed_num * 10 + r
    print(reversed_num)
else:
    print("sorry the number is less than 1000")

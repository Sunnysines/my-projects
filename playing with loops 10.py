"""now we have to cheak weather a given number is Armstrong number or
not
if a three digit number is equal to the sum of the cubes of its digits
then its Armstrong number.


"""
num = int(input("Enter a three digit number: "))
summ = 0
n = num
for i in range(1,4):
    digit = n % 10
    summ = summ + digit**3
    n = n // 10
if num == summ:
    print(num,"is a armstrong number")
else:
    print("it is not a armstrong number")

"""
ALTERNATIVE CODE
----------------

 num = int(input("Enter a three digit number: "))
summ = 0
n = num
while n > 0:
    digit = n % 10
    summ = summ + digit**3
    n = n // 10
if num == summ:
    print(num,"is a armstrong number")
else:
    print("it is not a armstrong number") """
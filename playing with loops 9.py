"""write a pogram to cheak weather a number is perfect number or not
a perfect number is a positive integer which is equal to its sum of its divisors


"""
n = int(input("Enter a number: "))
summ = 0
for i in range(1, n):
    if n % i == 0:
        summ += i
if summ == n:
    print(n, "is a perfect number")
else:
    print("its not a perfect number")

""" there are three different ways to find that the number is prime
or not the way i going to use is that i will take a number and then
take the half of it and then run a loop up to that number and find that
in between the loop the given number is divisible or not if it is
divisible then its prime number otherwise its not a prime number.




"""

n = 12
h = n//2
prime = bool
for i in range(2,h+1):
    if n % i == 0:
        prime = False
        break
else:
    prime = True
if prime == False:
    print("not prime")
else:
    print("prime")
"shortest  code"


"""def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    else:
        return True
"""



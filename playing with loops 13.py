"""now we have to calculate the HCF and LCM of the
the two numbers.

 things to remember is that:
PRODUCT OF THE NUMBERS = LCM * HCF


"""
s = 0
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    s = b
else:
    s = a
for i in range(1, s + 1):
    if a % i == 0 and b % i == 0:
        hcf = i
lcm = (a * b) / hcf
print("the HCF of", a, "and", b, "is", hcf)
print("the lcm of ", a, "and", b, "is", lcm)

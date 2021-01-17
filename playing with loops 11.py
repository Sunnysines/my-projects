"""Good work ,Now you have to write a pogram to find Armstrong number
between the limit given by the user.



"""
n = int(input("Enter the initial limit(of three digit number): "))
y = int(input("Enter the final limit(of three digit number): "))

a_num = 0
summ = 0

for i in range(n, y + 1):
    x = i
    summ = 0
    while x > 0:
        digit = x % 10
        summ = summ + digit ** 3
        x = x // 10
    digit = 0
    if summ == i:
        a_num += 1
        print(i)
if a_num != 0:
    print(a_num,"Armstrong number found")


else:
    print("no Armstrong number found")

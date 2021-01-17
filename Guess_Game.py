import random as r
secret_num = r.randint(1,100)
answer = int(input("Guess a number between 1 to 100: "))
while secret_num != answer:
    if answer > secret_num:
        print("you are close but the the number is too high")
        print("it was ",secret_num)
    else:
        print("you are close but don't you think its too low")
        print("it was ",secret_num)
    answer = int(input("Guess a number between 1 to 100: "))
    secret_num = r.randint(1, 100)
print("congratulations!you won")
print("it was ",secret_num)

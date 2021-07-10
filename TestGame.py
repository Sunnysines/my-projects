def main_menu():
    for i in range(1,15):
        if i%2 == 0:
            e = "even"
        else:
            e = "odd"
        if e == "even":
            if i==2:
                print("  |",end="                                       ")
                print(b.upper(),end="    ")
                print("                                      |")
                print("  |____________________________________________________________________________________________|")
            elif i==6:
                print("  |",end="                                       ")
                print(c.upper(),end="    ")
                print("                           |")
            elif i==8:
                print("  |",end="                                       ")
                print(d.upper(),end="    ")
                print("              |")
            elif i==10:
                print("  |",end="                                       ")
                print(f.upper(),end="    ")
                print("                           |")

        else:
            print("  |",end="                                                                            ")
            print("                |")
        e = None
    print("  |____________________________________________________________________________________________|")
    a = input("  Choose an option: ") 
    if a == "1":
        Game()
    if a == "2":
        options()
    if a == "3":
        exit()

#--------------------------------------------------------------------------------------------------
opt = "EASY"
def options():
    global opt
    diffculty = input("Please select you diffculty: ")
    if diffculty == "1":
         opt = "EASY"
         print("you have selected easy level")
    elif diffculty == "2":
         opt = "NORMAL"
         print("you have selected normal level")
    elif diffculty == "3":
         opt = "HARD"
         print("you have selected hard level")
    else:
        print("Difficulty is set to default(EASY)")
 #--------------------------------------------------------------------------------------------------       
def easy():
    import random as r
    answer = r.randint(1,50)
    n = int(input("Guess a number between 1-50: "))
    x = 0
    b = r.randint(1,2)
    
    while answer != n:
        if answer > n:
            print("it is a big number.")
            print(f"it was actually {answer}")
        else:
            print("it\'s samller than you think.")
            print("it was actully ",answer)
        x = answer
        n = int(input(f"Guess a number between {answer-b}-{x}: "))
        answer = r.randint(answer-b,answer)
    print("congrats you won :)")
    print("""you have beaten the easy level
    now you can try the other difficulty level
    """)
    g = input("by the way do you wanna play one more time?(y/n):")
    if g == "y":
        easy()
    elif g == "n":
        main_menu()
    else:
        main_menu()
#----------------------------------------------------------------------------------------------
def normal():
    import random as r
    answer = r.randint(1,100)
    n = int(input("Guess a number between 1-100: "))
    x = 0
    b = r.randint(1,10)
    
    while answer != n:
        if answer > n:
            print("it is a big number.")
            print(f"it was actually {answer}")
        else:
            print("it\'s samller than you think.")
            print("it was actully ",answer)
        x = answer
        n = int(input(f"Guess a number between 1-{x}: "))
        answer = r.randint(answer-b,answer)
    print("congrats you won :)")
    print("""you have done it, 
    you have won the normal level
    now you can try the other difficulty level
    """)
    g = input("by the way do you wanna play one more time?(y/n):")
    if g == "y":
        easy()
    elif g == "n":
        main_menu()
    else:
        main_menu()
#----------------------------------------------------------------------------------------------
def hard():
    import random as r
    answer = r.randint(1,100)
    n = int(input("Guess a number between 1-100: "))

    while answer != n:
        if answer > n:
            print("it is a big number.")
            print(f"it was actually {answer}")
        else:
            print("it\'s samller than you think.")
            print("it was actully ",answer)
        x = answer
        n = int(input(f"Guess a number between 1-100: "))
        answer = r.randint(answer,100)
    print("congrats you won :)")
    print("""hats off you are The Legendary Guess Master
    now you can try the other difficulty level
    """)
    g = input("by the way do you wanna play one more time?(y/n):")
    if g == "y":
        easy()
    elif g == "n":
        main_menu()
    else:
        main_menu()

#----------------------------------------------------------------------------------------------
def Game():
    print("welcome to the game i hope that, you know how to play :)")
    print("lets start/, ;) ")
    if opt == "EASY":
        easy()
    if opt == "NORMAL":
        normal()
    if opt == "HARD":
        hard()

print("""  ______________________________________________________________________________________________  """)
print("""  |                                                                                            |  """)
print("""  |         * * * *     *       *     * * * *     * * * *     * * * *                *         |  """)
print("""  |         *           *       *     *          *           *                      * *        |  """)
print("""  |         *   * **    *       *     * * * *     * * * *     * * * *              * * *       |  """)
print("""  |         *   *  *    *       *     *                  *            *           *     *      |  """)
print("""  |         ****   *    * * * * *     * * * *     * * * *     * * * *            *       *     |  """)
print("""  |                 9                           45                       12        0           |  """)
print("""  |       1                  59    3                       56                                  |  """)
print("""  |           2       6                       47                       3       1               |  """)
print("""  |                                                     20                                     |  """)
print("""  |   25    *     *    *       *    *       *    * * * *      * * * *     * * * *    19        |  """)
print("""  |         * *   *    *       *    * *   * *    *       *    *           *      *             |  """)
print("""  |         *  *  *    *       *    *   *   *    * * * *      * * * *     * *  * *             |  """)
print("""  |         *   * *    *       *    *       *    *       *    *           *   *                |  """)
print("""  |         *    **    * * * * *    *       *    * * * *      * * * *     *     *              |  """)
print("""  |                                                                                            |  """)
print("""  |                                                                                            |  """)
print("""  |____________________________________________________________________________________________|  """)


b = "|main menu|"
c = "play (press 1 to play)"
d = "options (press 2 to go to settings)"
f = "quit (press 3 to quit)"
e = None

main_menu()





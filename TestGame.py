import os

os.system("cls")
def refresh():
    os.system("cls")


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
        refresh()
        Game()
    elif a == "2":
        refresh()
        options()
    elif a == "3":
        exit()

#--------------------------------------------------------------------------------------------------
opt = "EASY"
def options():
    global opt
    global dif_c
    print("""                                     |OPTIONS|
                             HERE YOU CAN CHANGE THE DIFFICULTY LEVEL OF THE GAME.
                              choose any one of these.{easy-1,medium-2,hard-3} 
                            if you choose anything else it will be set to default(easy mode).
    """)
    diffculty = input("Please select you diffculty: ")
    if diffculty == "1":
         opt = "EASY"
         print("you have selected easy level :)")
         dif_c = "Easy"
         refresh()
         intro()
         main_menu()
    elif diffculty == "2":
         opt = "NORMAL"
         dif_c = "Normal"
         print("you have selected normal level :|")
         refresh()
         intro()
         main_menu()
    elif diffculty == "3":
         opt = "HARD"
         dif_c = "HARD!"
         print("you have selected hard level :[")
         refresh()
         intro()
         main_menu()
    else:
        print("Difficulty is set to default(EASY)")
        refresh()
        intro()
        main_menu()
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
        refresh()
        easy()
    elif g == "n":
        refresh()
        intro()
        main_menu()
    else:
        refresh()
        intro()
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
        normal()
    elif g == "n":
        refresh()
        intro()
        main_menu()
    else:
        refresh()
        intro()
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
        hard()
    elif g == "n":
        refresh()
        intro()
        main_menu()
    else:
        refresh()
        intro()
        main_menu()

#----------------------------------------------------------------------------------------------
def Game():
    print("welcome to the game i hope that, you know how to play :),difficulty "+dif_c)
    print("lets start/, ;) ")
    if opt == "EASY":
        easy()
    elif opt == "NORMAL":
        normal()
    elif opt == "HARD":
        hard()
def intro():

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
intro()
dif_c = "Easy"
b = "|main menu|"
c = "play (press 1 to play)"
d = "options (press 2 to go to settings)"
f = "quit (press 3 to quit)"
e = None

main_menu()





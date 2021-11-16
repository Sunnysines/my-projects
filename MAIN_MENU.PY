b = "|main menu|"
c = "play (press 1 to play)"
d = "options (press 2 to go to settings)"
f = "quit (press 3 to quit)"
e = None

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
main_menu()
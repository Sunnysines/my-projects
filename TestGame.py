print("""  ______________________________________________________________________________________________  """)
print("""  |                                                                                            |  """)
print("""  |       * * * *     *       *     * * * *     * * * *     * * * *                *           |  """)
print("""  |       *           *       *     *          *           *                      * *          |  """)
print("""  |       *   * **    *       *     * * * *     * * * *     * * * *              * * *         |  """)
print("""  |       *   *  *    *       *     *                  *            *           *     *        |  """)
print("""  |       ****   *    * * * * *     * * * *     * * * *     * * * *            *       *       |  """)
print("""  |               9                           45                       12        0             |  """)
print("""  |     1                  59    3                       56                                    |  """)
print("""  |         2       6                       47                       3       1                 |  """)
print("""  |                                                   20                                       |  """)
print("""  | 25    *     *    *       *    *       *    * * * *      * * * *     * * * *    19          |  """)
print("""  |       * *   *    *       *    * *   * *    *       *    *           *      *               |  """)
print("""  |       *  *  *    *       *    *   *   *    * * * *      * * * *     * *  * *               |  """)
print("""  |       *   * *    *       *    *       *    *       *    *           *   *                  |  """)
print("""  |       *    **    * * * * *    *       *    * * * *      * * * *     *     *                |  """)
print("""  |                                                                                            |  """)
print("""  |                                                                                            |  """)
print("""  |____________________________________________________________________________________________|  """)


b = "|main menu|"
c = "play (press 1 to play)"
d = "options (press 2 to go to settings)"
f = "quit (press 3 to quit)"
e = None
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


a = input("Enter something: ")





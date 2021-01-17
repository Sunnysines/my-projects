"""write a pogram in python to print the following pattern without
using nested loops.

4321
432
43
4

"""
"""n = 0
for i in range(1,5):
    for j in range(4,n,-1):
        print(j,end="")
    print()
    n += 1
"""

for i in range(4):
    for j in range(4, i, -1):
        print(j, end="")
    print()

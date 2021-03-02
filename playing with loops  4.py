""" In this question you will have to print thhe following pattern
for loop

APQR
ABQR
ABCR
ABCD


man this loop seems to be hard.Lets see ho to solve it.
ABCD
0123

"""
str1 = 'ABCD'
str2 = 'PQR'
for i in range(4):
    print(str1[: i + 1] + str2[i:])
"""this is the answer i got from some were,hmm 
i do have to know the string part 
for this type of pogram"""

""" we have to print the first 20 element of the fibonaki series
  0 1 1 2 3 5 8
  0+1 = 1
  1+1 = 2
  2+1 = 3
  2+3 = 5
...
and its go on.
so.

 """
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(20):
    s = n1 + n2
    n1 = n2
    n2 = s
    print(s)


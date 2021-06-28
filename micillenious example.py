l = [2,2,3,5,6,3,9,2,9]
   # 0 1 2 3 4 5 6 7 8
a = len(l)
for i in l:
    for j in range(1,a):
        print(l[j])
        if i == l[j]:
            l.pop(j)
            a = len(l)
print(l)
s = 100000
r = 0
st = ""
while s > 0:
    r = s % 16
    s = s // 16
    if r < 9:
        st = str(r) + st
    else:
        st = str(chr(87 + r)) + st
        s = s // 16
print(st)

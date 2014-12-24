f_read = open('a.txt', 'r')
v = None
for line in f_read:
    k = int(line)
    if v != None:
        if k > v:
                v = k
    else:
        v = k
print(v)
f_read.close()

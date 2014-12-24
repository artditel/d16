f_read = open('a.txt', 'r')
a = [None, None, None, None, None, None, None, None, None, None]
for line in f_read:
    k = int(line)
    if a[0] != None:
        for x in range(9):
            if a[x] < k:
                    if a[x] != None:
                        for l in range(9 - x):
                            a[9 - l] = a[8 - l]
                        else:
                            a[x] = k




    else:
        a[0] = k
print(a)
f_read.close()

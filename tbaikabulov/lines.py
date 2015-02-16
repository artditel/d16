def f(line):
	line=line.split()
	print(line)
	print(len(line[-1]))
	return int(line[-2]), int(line[-1][0])-int(line[-1][2]) if len(line[-1])==3 else 0
summfalse=0
summeq=0
summtrue=0
nfalse=0
neq=0
ntrue=0
with open("file") as file1:
    for l in file1:
    	summ+=f(line)[0] if f(line[1]
    	n+=1

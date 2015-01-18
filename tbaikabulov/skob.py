k=input()
s=''
for i in range(0,len(k)):
    s+=k[i]
    if len(s)>1:
        if (s[-1]==')' and s[-2]=='(') or (s[-1]=='}' and s[-2]=='{') or (s[-1]==']' and s[-2]=='['):
            s=s[:-2]
if s=='':
    print('yes')
else:
    print('no')

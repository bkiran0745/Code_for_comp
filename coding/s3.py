s=input()
d={}
for i in s:
    if i in d:
        d[i]=1
    else:
        print(i)
        break
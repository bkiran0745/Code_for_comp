n=int(input())
res=1
for i in range(1,n+1):
    for j in range(i):
        print(res,end=" ")
        res+=1
    print()
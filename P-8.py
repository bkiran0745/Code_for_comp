n = int(input())
arr = list(map(int,input().split()))
temp=[]
for i in range(len(arr)):
    if i == 0:
        temp.append(arr[i])
    else:
        for j in range(i,len(arr)):
            if temp[-1]*3 == arr[j]:
                temp.append(arr[j])
print(len(temp))
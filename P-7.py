n = int(input())
arr = list(map(int,input().split()))
k = int(input())
temp =[]
for i in range(len(arr)):
    if i == 0:
        temp.append(arr[i])
    else:
        for j in range(i,len(arr)):
            if abs(arr[j]-temp[-1]) % k == 0:
                temp.append(arr[j])
            else:
                print("Not entered")
print(len(temp))
print(temp)
temp = [arr[0]]
for j in range(1,len(arr)):
    if abs(arr[j]-temp[-1]) % k == 0:
        temp.append(arr[j])
    else:
        print("Not entered")
print(len(temp))
print(temp)
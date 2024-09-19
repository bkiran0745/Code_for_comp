def InversionCount(A,n):
    count = 0
    if len(A)==0:
        return -1
    if n<2:
        return 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if arr[i]>arr[j]:
                count+=1
    return count
    
n = int(input())
arr = list(map(int,input().split()))
print(InversionCount(set(arr),n))
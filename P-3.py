def FindNumberOfSuperiorElements(arr,n):
    maxi = -1
    count = 0
    for i in range(len(arr)-1,-1,-1):
        if maxi < arr[i]:
            count+=1
            maxi = arr[i]
    return count    
n = int(input())
arr = list(map(int,input().split()))
print(FindNumberOfSuperiorElements(arr,n))
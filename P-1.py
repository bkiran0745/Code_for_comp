def SumOddIntegers(arr,n):
    sum = 0
    for i in range(len(arr)):
        if arr[i]%2 != 0:
            sum += arr[i]
    return sum
n = int(input())
arr = list(map(int,input().split()))
print(SumOddIntegers(arr,n))


def OperationsBinaryString(arr):
    sol=int(arr[0])
    for i in range(len(arr)):
        if not arr[i].isdigit():
            if arr[i] == 'A':
                sol=sol&int(arr[i+1])
            if arr[i] == 'B':
                sol=sol|int(arr[i+1])
            if arr[i] == 'C':
                sol=sol^int(arr[i+1])
    return sol
arr = input()
print(OperationsBinaryString(arr))
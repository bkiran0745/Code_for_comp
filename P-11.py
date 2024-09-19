def CheckPassword(arr,n):
    capi=0
    num=0
    for i in range(len(arr)):
        if arr[0].isdigit() or len(arr)<4:
            return 0
        if ord(arr[i])>=65 and ord(arr[i])<=90:
            capi=1
        if arr[i]==' ' or arr[i]=='/':
            return 0
        if arr[i].isdigit():
            num=1
    if capi==1 and num==1:
        return 1
    return 0
n=int(input())
arr=input()
print(CheckPassword(arr,n))
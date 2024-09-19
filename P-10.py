def Substring(arr):
    maxi = ''
    if len(arr) == 1:
        return arr
    def Max_Sub(left,right):
        while left>=0 and right<len(arr) and arr[left] == arr[right]:
            left-=1
            right+=1
        return arr[left+1:right]
    for i in range(len(arr)):
        even_palw = Max_Sub(i,i+1)
        if len(even_palw) > len(maxi):
            maxi = even_palw
        odd_palw = Max_Sub(i,i)
        if len(odd_palw) > len(maxi):
            maxi = odd_palw
    return maxi
arr=input()
print(Substring(arr))
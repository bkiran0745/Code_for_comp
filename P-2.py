n = int(input())
while n>9:
    if n%2 == 0:
        n=(n-2)/2
    else:
        n=n/2
print(int(n))
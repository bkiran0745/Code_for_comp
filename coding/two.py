k = int(input())
if k<=3:
    print(1)
else:
    prod = 1
    while k>4:
        prod*=3
        k-=3
    prod*=k
    print(prod)
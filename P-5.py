n = int(input())
plane = 1
if (0<=n<=100):
    for i in range(n):
        plane += (i+1)
print(plane)

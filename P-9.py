Str = input()
Str2=''
for i in range(len(Str)-1,-1,-1):
    Str2+=Str[i]
str3 = Str[::-1]
if Str == Str2:
    print(True)
    print(str3)
else:
    print(False)
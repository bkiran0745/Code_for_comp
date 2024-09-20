
def lo():
    s = input()
    d= []
    for char in s:
        if char not in d:
            d.append(char)
        else:
            return char
print(lo())
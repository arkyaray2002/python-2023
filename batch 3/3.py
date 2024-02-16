def count_f(st):
    f = [0] * 256
    for char in st:
        f[ord(char)] += 1
    return f

s = input("Enter a string: ")
f = count_f(s)
for char,freq in enumerate(f):
    if freq != 0:
        print(f"Count of {chr(char)} : {freq}")

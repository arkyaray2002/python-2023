def return_anagram(li, st):
    res = filter(lambda x: sorted(x) == sorted(st), li)
    return list(res)

li = input("Enter the list of strings: ").split()
s = input("Enter the required string")
print(return_anagram(li,s))
    



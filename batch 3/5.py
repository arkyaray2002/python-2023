def check_heterogram(s):
    check = []
    for each in s.replace(' ', ''):
        if each not in check:
            check.append(each)
        else:
            return False

    return True

s = input("Enter a string")
print('Yes') if check_heterogram(s) else print('No')

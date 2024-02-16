# method 1

def ends_with_6(num):
    return True if num%10 == 6 else False

def divisible_by_7(num):
    return True if num%7 == 0 else False

def check_range(num):
    li = []
    for i in range(1,num):
        if ends_with_6(i) and divisible_by_7(i) == True:
            li.append(i)
    return li
n = int(input("Enter the range : "))
print(f"list of numbers: {check_range(n)}\nCount: {len(check_range(n))}")


# method 2

li2 = []
for i in range(0, n, 7):
    if i%10 == 6 : li2.append(i) 
print(f"list of numbers : {li2}\nCount: {len(li2)}")

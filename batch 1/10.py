def check_magic(num):
    if not isinstance(num, int):
        print("Invalid input")
        return False
    if len(str(num)) == 1:
        return True if num == 1 else False
    sum_ = sum(list(map(int, list(str(num)))))
    return check_magic(sum_)


n = int(input("Enter a number: "))
print(check_magic(n))


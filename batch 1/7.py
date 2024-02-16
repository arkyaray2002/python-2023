def hcf_recursive(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
        return hcf_recursive(num1-num2, num2)
    else:
        return hcf_recursive(num1, num2-num1)

li = list(map(int, input("Enter elements: ").split()))
try:
    val1 = li[0]
    val2 = li[4]
    if val1 or val2 <=0:
        raise ValueError
    print(hcf_recursive(val2, val1))
except IndexError:
    print("Not enough elements")
except ValueError:
    print("No negative values")
except NameError:
    print("Invalid variable name")

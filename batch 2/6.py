def list_of_factors(n):
    if n <= 0:
        raise ValueError
    count = []
    for i in range(1, n+1):
        if n % i == 0:
            count.append(i)
    return count

def number_of_factors(n):
    return len(list_of_factors(n))

try:
    n = int(input("Enter a number"))
    li = list_of_factors(n)
    count = number_of_factors(n)
except ValueError:
    print("Enter a positive value")
else:
    print(f"number of factors : {count}\nlist of factors : {li}")

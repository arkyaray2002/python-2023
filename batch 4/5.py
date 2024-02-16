def print_diamond(n):
    for i in range(n+1):
        for j in range(n-i):
            print(end = " ")
        for j in range(i):
            print('* ', end = "")
        print()
    for i in range(n-1, -1, -1):
        for j in range(n-i):
            print(end = " ")
        for i in range(i):
            print('* ', end= "")
        print()

def is_prime(n):
    return len([x for x in range(1,n+1) if n%x == 0]) == 2

print_diamond(4)
print(is_prime(36))

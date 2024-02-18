import sys
a = int(sys.argv[1])
b = int(sys.argv[2])

def check_fibonacci(n):
    a = 0
    b = 1
    c = 0
    while c < n:
        c = a + b
        a = b
        b = c
    return False if c != n else True
        
def check_prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return True if count == 2 else False


for i in range(a, b+1):
    if check_fibonacci(i) == False and check_prime(i) == False:
        print(i)

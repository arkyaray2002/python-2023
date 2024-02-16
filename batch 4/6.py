def gcd(n1, n2):
    if n1 == n2:
        return n1
    elif n1 > n2:
        return gcd(n1-n2, n2)
    else:
        return gcd(n1, n2-n1)

def lcm(n1,n2):
    return (n1*n2)//gcd(n1,n2)

print(gcd(12,32),lcm(12,32))

x = lambda a : a + 15

print(x(9))

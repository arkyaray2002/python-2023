def armstrong(n):
    pow = len(str(n))
    if sum(list(map(lambda x : x ** pow, list(map(int, list(str(n))))))) == n:
        return True
    else:
        return False

print(armstrong(153))

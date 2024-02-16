def harmonic_sum(n):
    s = 0
    for i in range(1, n):
        s += 1/i
    return round(s, 2)

print(harmonic_sum(10))

def zeros(n):
    if n <= 0:
        return 0
    else:
        i = 0
        while n >= 5:
            n //= 5
            i += n
        return i

assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7


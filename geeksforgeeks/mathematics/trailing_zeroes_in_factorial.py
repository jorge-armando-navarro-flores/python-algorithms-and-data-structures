def trailing_zeroes_in_factorial(n):
    res = 0
    while n >= 5:
        n //= 5
        res += n
    return res

n = 10
print(trailing_zeroes_in_factorial(n))
       
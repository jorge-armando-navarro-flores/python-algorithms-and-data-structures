import math

def digits_in_factorial(n):
    res = 0
    for i in range(2, n+1):
        res += math.log10(i)
    return math.floor(res) + 1

n = 5

print(digits_in_factorial(5))
def gp_term(a, b, n):
    r = b / a
    return a * r ** (n - 1)

a = 84
b = 87
n = 3

print(gp_term(a, b, n))
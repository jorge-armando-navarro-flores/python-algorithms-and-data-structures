def modular_multiplicative_inverse(a, m):
    for i in range(1, m+1):
        if (i * a) % m == 1:
            return i
    return -1

a = 3
m = 11

print(modular_multiplicative_inverse(a, m))
   
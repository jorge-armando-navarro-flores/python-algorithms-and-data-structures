import math

def quadratic_ecuation_root(a, b, c):
    ecuation = b**2 - 4 * a * c
    if ecuation < 0:
        return "Imaginary"
    square_root = math.sqrt(ecuation)
    x1 = (-b + square_root) / (2 * a)
    x2 = (-b - square_root) / (2 * a)
    return math.floor(x1), math.floor(x2)
    # ans.sort(reverse=True)
    # return ans

a = -264
b = -750
c = 504

print(quadratic_ecuation_root(a, b, c))
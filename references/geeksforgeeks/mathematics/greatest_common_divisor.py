def greatest_common_divisor(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def greatest_common_divisor_optimized(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)

a = 7
b = 13

print(greatest_common_divisor_optimized(a, b))
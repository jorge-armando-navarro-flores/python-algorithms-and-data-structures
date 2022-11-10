def gratest_common_divisor(a, b):
    if b == 0:
        return a
    return gratest_common_divisor(b, a % b)

def lowest_common_multiple_of_two_numbers(a, b):
   return a * b // gratest_common_divisor(a, b)

a = 12
b = 15

print(lowest_common_multiple_of_two_numbers(a, b))
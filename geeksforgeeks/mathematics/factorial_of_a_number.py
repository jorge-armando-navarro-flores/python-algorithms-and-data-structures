def factorial_of_a_number(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    return factorial

def factorial_of_a_number_recursive(n):
    if n == 0:
        return 1
    return n * factorial_of_a_number_recursive(n - 1)
n = 4

print(factorial_of_a_number_recursive(n))
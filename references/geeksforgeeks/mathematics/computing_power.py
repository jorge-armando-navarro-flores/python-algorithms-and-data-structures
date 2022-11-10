def computing_power(x, n):

    if n == 0:
        return 1


    if n % 2 == 0:
        return computing_power(x, n // 2) * computing_power(x, n // 2)
    else:
        return computing_power(x, n-1) * x

def computing_power_iterative(x, n):
    res = 1
    while n > 0:
        if n % 2 != 0:
            res *= x
        x *= x
        n = n // 2

    return res
        

x = 4
n = 5
print(computing_power_iterative(x, n))
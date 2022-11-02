def fun1(n):
    return n * (n+1) // 2

def fun2(n):
    numbers_sum = 0
    for i in range(1, n+1):
        numbers_sum += i

    return numbers_sum

n = int(input("Enter n: "))
sum = fun1(n)
print("Sum is:", sum)

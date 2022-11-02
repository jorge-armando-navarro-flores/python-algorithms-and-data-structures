def count_digits(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count

n = int(input("Enter n: "))
res = count_digits(n)
print("num of digits is:", res)
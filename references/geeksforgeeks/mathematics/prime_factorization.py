def prime_factorization(n):
    while n % 2 == 0:
        print(2, end=' ')
        n //= 2

    while n % 3 == 0:
        print(3, end=' ')
        n //= 3

    divisor = 5
    while n != 1:
        while n % divisor == 0:
            print(divisor, end=' ')
            n //= divisor

        while n % (divisor + 2) == 0:
            print(divisor + 2, end=' ')
            n //= (divisor + 2)
        
        divisor += 6

n = 13
prime_factorization(n)


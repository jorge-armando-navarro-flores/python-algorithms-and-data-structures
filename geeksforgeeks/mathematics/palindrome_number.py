

from operator import neg


def palindrome_number(n):
    rev = 0
    temp = n
    while temp != 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp //= 10
    return rev == n

n = 78987

print(palindrome_number(n))








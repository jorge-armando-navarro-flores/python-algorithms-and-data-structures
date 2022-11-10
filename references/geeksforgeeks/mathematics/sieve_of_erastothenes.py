def sieve_of_eratosthenes2(n):
    if 2 <= n:
        print(2, end=' ')
    if 3 <= n:
        print(3, end=' ')

    i = 5
    while i <= n:
        if n % i != 0:
            print(i, end=' ')
        if i + 2 <= n:
            print(i + 2, end=' ')
        i += 6

def sieve_of_eratosthenes(num):
	prime = [True for i in range(num+1)]
	p = 2
	while (p * p <= num):

		if (prime[p] == True):

			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1

	for p in range(2, num+1):
		if prime[p]:
			print(p, end=' ')


n = 1000
sieve_of_eratosthenes(n)
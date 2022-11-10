def check_for_prime(n):
	if n == 1:
		return False
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False

	i = 5
	while i * i <= n:
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

def exactly_3_divisors(n):
	divisors = 0
	i = 2
	while i * i <= n:
		if check_for_prime(i) and i * i <= n:
			divisors += 1
		i += 1
	return divisors

	
n = 10
print(exactly_3_divisors(n))

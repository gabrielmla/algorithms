def power(n, pow):
	if pow == 0:
		return 1
	elif pow % 2 == 0:
		return power((n * n) % (2**31 - 1), pow/2)
	else:
		return (power(n, pow-1) * n)
			
b = input()

print power(3,b) % (2**31 - 1)

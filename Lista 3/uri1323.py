while True:
	n = input()
	if n == 1:
		print n
	elif n > 1:
		total = 1
		while n >= 2:
			total += n * n
			n -= 1
		print total
	else:
		break

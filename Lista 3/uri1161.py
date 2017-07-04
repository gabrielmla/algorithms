def fatorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fatorial(n-1)

while True:
	try:
		n, m = map(int, raw_input().split())
		print fatorial(n) +  fatorial(m)
	except EOFError: break

n, a, b, c = map(int, raw_input().split())

if n % 4 == 0:
	print 0
elif n % 2 == 0:
	print min(2*a,b,2*c)
else:
	if n % 4 == 1:
		print min(3*a,b+a,c)
	else:
		print min (a, b+c, 3*c)


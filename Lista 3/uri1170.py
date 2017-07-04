n = input()

for i in xrange(n):
	a = float(raw_input())
	d = 0
	while a > 1.0:
		a /= 2.0
		d += 1
	print "%d dias" % d

n = input()

for i in xrange(n):
	s = raw_input()
	lS = len(s)
	
	esq = s[:lS/2]
	esq = esq[::-1]
	dir = s[(lS/2):]
	dir = dir[::-1]
	
	print esq + dir

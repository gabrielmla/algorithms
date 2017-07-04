q = input()
for i in xrange(q):
	n = input()
	cidades = dict.fromkeys(range(n))
	for j in xrange(n):
		c = map(int, raw_input().split())
		cidades[j] = c
	

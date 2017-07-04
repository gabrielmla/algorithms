n = input()
nomes = []
comp = []
for i in xrange(n):
	c, s = raw_input().split()
	nomes.append(s)
	comp.append(c)
	
nomes.sort()

for c in nomes:
	print c
bom = comp.count("+")
mal = comp.count("-")
print "Se comportaram: %d | Nao se comportaram: %d" % (bom, mal)

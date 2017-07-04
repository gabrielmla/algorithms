n = input()
saps = {}
for i in xrange(n):
	m, l = raw_input().split()
	if saps.has_key(m):
		saps[m].append(l)
	else:
		saps[m] = l
print saps

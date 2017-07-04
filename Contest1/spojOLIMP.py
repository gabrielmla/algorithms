import operator
n, m = map(int, raw_input().split())
cla = dict.fromkeys(range(n))
print cla
for i in xrange(m):
	l = map(int, raw_input().split())
	for j in l:
		if cla[j-1] == None:
			cla[j-1] = 1
		else:
			cla[j-1] += 1
sorted_cla = sorted(cla.items(), key=operator.itemgetter(1), reverse = True)

for i in sorted_cla:
	print i[0] + 1,

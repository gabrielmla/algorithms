s = raw_input()
lS = len(s)
res = [s]
for i in xrange(lS):
	a = s[0:-1]
	b = s[lS - 1] + a
	if b not in res:
		res.append(b)
		s = b

print len(res)

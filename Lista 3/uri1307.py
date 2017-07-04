n = input()

def mdc(a, b):
	if b == 0:
		return a
	else:
		return mdc(b, a%b)

for i in range(n):
	s1 = raw_input()
	s1 = int(s1, 2)
	s2 = raw_input()
	s2 = int(s2, 2)
	if mdc(s1, s2) == 1:
		print "Pair #%d: Love is not all you need!" % (i + 1)
	else:
		print "Pair #%d: All you need is love!" % (i + 1)

n = input()
fn = {}
for i in xrange(n):
	l = raw_input()
	fn[l] = raw_input()

m = input()
for i in xrange(m):
	c = raw_input()
	l = raw_input()
	print c
	print fn[l]
	print

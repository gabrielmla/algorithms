n = input()

def mdc(a, b):
	if b == 0:
		return a
	else:
		return mdc(b, a%b)

for i in xrange(n):
	f1, f2 = map(int, raw_input().split())
	print mdc(f1, f2)

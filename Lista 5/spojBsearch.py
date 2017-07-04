def bSearch(a, i, f, e):
	meio = (i + f) / 2
	if (a[meio] == e):
		return meio
	if i >= f:
		return -1
	else:
		if a[meio] < e:
			return bSearch(a, meio + 1, f, e)
		else:
			return bSearch(a, i, meio - 1, e)

n, q = map(int, raw_input().split())
a = map(int, raw_input().split())

for i in xrange(q):
	print bSearch(a, 0, n - 1, input())

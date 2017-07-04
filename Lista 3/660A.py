n = input()
a = map(int, raw_input().split())
k = 0
c = []
def mdc(a, b):
	if b == 0:
		return a
	else:
		return mdc(b, a%b)

for i in range(n-1):
	c.append(a[i])
	if mdc(a[i], a[i+1]) != 1:
		k += 1
		c.append(1)
c.append(a[n-1])
print k
for j in c:
	print j,

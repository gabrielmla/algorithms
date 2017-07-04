import math
# Precalculo de primos
n = 10**6
prime = [True] * (n + 1)
prime[0] = False
prime[1] = False
m = int(math.sqrt(n))

for i in range(2, m+1, 1):
	if (prime[i]):
		for k in range(i+i, n+1, i):
			prime[k] = False

# Precalculo de primos xemeos
xemeos = [0, 0]
cXemeos = 0
for p in range(2, n - 2):
	if prime[p]:
		if prime[p - 2] or prime[p + 2]:
			cXemeos += 1
	xemeos.append(cXemeos)
xemeos.append(cXemeos)
xemeos.append(cXemeos)
xemeos.append(cXemeos)

# Problema em si
q = input()
for i in range(q):
	x, y = map(int, raw_input().split())
	if y > x:
		print xemeos[y] - xemeos[x-1]
	else:
		print xemeos[x] - xemeos[y-1]

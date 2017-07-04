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
# Problema
n, m = map(int, raw_input().split())
mA = []
Rmoves = 0
Cmoves = 0

for i in xrange(n):
	mA.append(map(int, raw_input().split()))
	
for i in xrange(m):
	aumento = 0
	while not prime[mA[0][i]]:
		mA[0][i] += 1
		aumento += 1
		Rmoves += 1
	mA[0][i] -= aumento

for j in xrange(n):
	aumento = 0
	while not prime[mA[j][0]]:
		mA[j][0] += 1
		aumento += 1
		Cmoves += 1
	mA[j][0] -= aumento

print min(Cmoves, Rmoves)

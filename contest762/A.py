import math

n, k = map(int, raw_input().split())
div = [1]
diva = []
i = 2
while i <= math.sqrt(n):
	if n % i == 0:
		div.append(i)
		if i != n/i:
			diva.append(n/i)
	i += 1

for i in diva[::-1]:
	div.append(i)
	
if k > len(div):
	print -1
else:
	print div[k-1]
		

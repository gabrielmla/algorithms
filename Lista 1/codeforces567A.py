n = input()
cities = map(int, raw_input().split())

for i in xrange(n):
	if i == 0:
		minimo = abs(cities[i] - cities[i+1])
		maximo = abs(cities[i] - cities[-1])
	elif i == n - 1:
		minimo = abs(cities[i] - cities[i-1])
		maximo = abs(cities[i] - cities[0])
	else:
		min1 = abs(cities[i] - cities[i+1])
		min2 = abs(cities[i] - cities[i-1])
		minimo = min(min1, min2)
		max1 = abs(cities[i] - cities[0])
		max2 = abs(cities[i] - cities[-1])
		maximo = max(max1, max2)
	
	print "%d %d" % (minimo, maximo)
		


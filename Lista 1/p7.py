n = input()
cities = map(int, raw_input().split())

for i in cities:
	mins = []

	for j in xrange(n):
		if cities[j] != i:
			mins.append(abs(i - cities[j]))
	
			
	print "%d %d" % (min(mins), max(mins))

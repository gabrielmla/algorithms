n, a, b = map(int, raw_input().split())
ap = raw_input()
cost = 0

atual = ap[a-1]
destino = ap[b-1]

if a != b:
	if atual == destino:
		print 0
	else:
		print 1
else:
	print 0

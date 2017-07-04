while True:
	try:
		n = input()
		saps = {}
		total = 0
		for i in xrange(n):
			m, l = raw_input().split()
			if saps.has_key(m):
				saps[m].append(l)
			else:
				saps.setdefault(m, [l])
		for s in saps:
			d = 0
			e = 0
			for l in saps[s]:
				if l == "D":
					d += 1
				else:
					e += 1
			total += min(d, e)
		print total
	except:
		break

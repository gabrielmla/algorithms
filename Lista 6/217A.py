n = input()
snow_drifts = []
vis = []
componentes = 0

for i in xrange(n):
	i, j = map(int, raw_input().split())
	snow_drifts.append((i, j))

def driftando(snow):
	if snow in vis:
		return
	else:
		vis.append(snow)
		auxSnow = snow_drifts[:]
		auxSnow.remove(snow)

		for snowD in auxSnow:
			if snowD[0] == snow[0] or snowD[1] == snow[1]:
				driftando(snowD)

for snow in snow_drifts:
	if snow not in vis:
		driftando(snow)
		componentes += 1

print componentes - 1

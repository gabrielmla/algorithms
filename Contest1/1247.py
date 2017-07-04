import math
while True:
	try:
		d, vf, vg = map(int, raw_input().split())
		h = math.sqrt(d**2 + 12**2)
		f = 12.0/vf
		g = h/vg
		if g <= f:
			print "S"
		else:
			print "N"
	except:
		break

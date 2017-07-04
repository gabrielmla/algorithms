s = raw_input()
kr = 0
kb = 0
ky = 0
kg = 0
cores = "RGYB"
for i in xrange(len(s)):
	if s[i] == "!":
		auxL = ""
		auxR = ""
		nope = ""
		if (i + 3) < len(s):
			for j in xrange(1, 4):
				auxR += s[i+j]
		if (i - 3) >= 0 :
			for j in xrange(1, 4):
				auxL += s[i-j]
		if len(auxL) > 0:
			for j in auxL:
				if j not in nope:
					nope += j
		if len(auxR) > 0:
			for j in auxR:
				if j not in nope:
					nope += j
		for l in cores:
			if l not in nope:
				if l == "R":
					kr += 1
				elif l == "G":
					kg += 1
				elif l == "Y":
					ky += 1
				elif l == "B":
					kb += 1
		print auxL, auxR
		print nope
		print kr,kb,ky,kg

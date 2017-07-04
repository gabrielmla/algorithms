n = input()

while n != 0:
	music = map(int, raw_input().split())
	music.append(music[0])
	nLoop = 0

	status = []
	for i in xrange(n):
		if music[i] < music[i+1]:
			status.append("s")
		elif music[i] > music[i+1]:
			status.append("d")
		
		if status[i-1] != status[i]:
			nLoop += 1
	if status[-1] != status[0]:
		nLoop += 1
	print nLoop
	n = input()

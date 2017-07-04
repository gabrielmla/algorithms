casos = []

def find_home(casos, j):
	for i in casos:
		if i[0] == j[0] or i[1] == j[1]:
			print "divisa"
		elif j[0] > i[0]:
			if j[1] > i[1]:
				print "SO"
			else:
				print "NO"
		elif j[0] < i[0]:
			if j[1] > i[1]:
				print "SE"
			else:
				print "NE"

while True:
	k = input()
	if k == 0:
		break
		
	ponto_divisor = map(int, raw_input().split())
	for i in xrange(k):
		casos.append(map(int, raw_input().split()))
	find_home(casos, ponto_divisor)
	casos = []

participantes = []
teste = 0

def ganhador(participantes, n):
	for i in xrange(n):
		if i + 1 == participantes[i]:
			return participantes[i]
		
	return 0
		
while True:
	teste += 1
	n = input()
	
	if n == 0:
		break
	
	participantes = (map(int, raw_input().split()))
	
	print "Teste %d" % teste
	print ganhador(participantes, n)
	print ""
	

from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
n = input()
casas = [0] * n 
visitado = [False] * n
total_visitado = 0
deuRuimTM = False

for i in xrange(n):
	linha = raw_input()
	if not visitado[i]:
		visitado[i] = True
		casas[i] += 1
		total_visitado += 1
		for j in xrange(n):
			if i != j:
				if not visitado[j]:
					if linha[j] == 'S':
						visitado[j] = True
						casas[i] += 1
						total_visitado += 1
	else:
		for j in xrange(n):
			if i != j:
				if linha[j] == 'S':
					deuRuimTM = True
				else:
					visitado[j] = True
					casas[i] += 1
					total_visitado += 1

print "Casas:", casas
print "Visitado:", visitado
print "Total:", total_visitado
print "Deu ruim?", deuRuimTM

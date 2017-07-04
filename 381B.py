n, m = map(int, raw_input().split())

a = map(int, raw_input().split())
emes = []
positivo = []

def somaAcumulada(array):
	soma = 0
	for i in array:
		soma += i
	return soma
for i in range(m):
	emes.append(map(int, raw_input().split()))
for j in emes:
	soma = somaAcumulada(a[j[0]-1:j[1]])
	if soma > 0:
		positivo.append(soma)
total = 0
for k in positivo:
	total += k
print total


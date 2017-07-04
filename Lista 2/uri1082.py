# Recebendo e ordenando a entrada
po = map(int, raw_input().split())
nP = po.pop(0)
po.sort(reverse = True)
ma = map(int, raw_input().split())
nM = ma.pop(0)
ma.sort(reverse = True)
fi = map(int, raw_input().split())
nF = fi.pop(0)
fi.sort(reverse = True)
qu = map(int, raw_input().split())
nQ = qu.pop(0)
qu.sort(reverse = True)
bi = map(int, raw_input().split())
nB = bi.pop(0)
bi.sort(reverse = True)

# Sets de livros
k = []
nK = input()
a = 0
b = 0
c = 0
d = 0
e = 0
while a < nP:
	while b < nM:
		soma = po[a] + ma[b] + fi[c] + qu[d] + bi[e]
		k.append(soma)
		b += 1
	b = 0
	c = 1
	while c < nF:
		soma = po[a] + ma[b] + fi[c] + qu[d] + bi[e]
		k.append(soma)
		c += 1
	c = 0
	d = 1
	while d < nQ:
		soma = po[a] + ma[b] + fi[c] + qu[d] + bi[e]
		k.append(soma)
		d += 1
	d = 0
	e = 1
	while e < nB:
		soma = po[a] + ma[b] + fi[c] + qu[d] + bi[e]
		k.append(soma)
		e += 1
	e = 0
	a += 1


k.sort(reverse = True)
t = k[:]
w = k
print t
print w
soma = 0
i = 0
while i < nK and i < len(k):
	soma += k[i]
	i += 1
if nK != 1:
	print soma + 1
else:
	print soma

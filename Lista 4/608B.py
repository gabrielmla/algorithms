import math
a = raw_input()
b = raw_input()
la = len(a)
lb = len(b)
soma = 0

for j in xrange(la):
    n = int(a[j])
    for i in xrange(lb - la + 1):
        soma += abs(n - int(b[i + j]))

print soma

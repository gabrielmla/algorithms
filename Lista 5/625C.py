n, k = map(int, raw_input().split())
sTable = [[0] * 500 for x in xrange(500)]
maiorNum = n**2
k -= 1
# Preenchendo colunas de um lado
for i in xrange(n):
    for j in xrange(n-1, k-1, -1):
        sTable[i][j] = maiorNum
        maiorNum -= 1
# Preenchendo colunas de um lado(se precisar)
for i in xrange(n):
    for j in xrange(k-1, -1, -1):
        sTable[i][j] = maiorNum
        maiorNum -= 1

soma = 0
for i in xrange(n):
    soma += sTable[i][k]
print soma

for i in xrange(n):
    for j in xrange(n):
        print sTable[i][j],
    print


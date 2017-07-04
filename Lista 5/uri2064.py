# Quantidade de letras favoritas
def q_fav(s, f):
    nfav = 0
    for i in s:
        if i in f:
            nfav += 1
    return nfav

# Realiza a troca de letras
def troca_fav(s, m, a, b):
    aux = ""
    for l in xrange(m):
        if s[l] == a:
            aux += b
        elif s[l] == b:
            aux += a
        else:
            aux += s[l]
    return aux

# Entrada
k, m, n = map(int, raw_input().split())
fav = raw_input()
n_atual = raw_input()
nomes = {}
nomes.setdefault(q_fav(n_atual, fav), [n_atual])

# Preenchendo o dicionario na forma key = q_fav e value = troca_fav
for i in xrange(n):
    a, b = raw_input().split()
    n_atual = troca_fav(n_atual, m, a, b)
    nfav = q_fav(n_atual, fav)
    if nomes.has_key(nfav):
        nomes[nfav].append(n_atual)
    else:
        nomes.setdefault(q_fav(n_atual, fav), [n_atual])

maior = max(nomes.iterkeys())
print maior
print nomes
print nomes[maior][0]

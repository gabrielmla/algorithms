n, m = map(int, raw_input().split())
cont = 0

if m < n: #so vou poder chegar no numero fazendo subtracao
    cont = n - m
else:
    while m > n:
        if m % 2: # se m nao for par, incrementa um pra ele ser par
            m += 1
            cont += 1
        # dividir m por 2 sempre que ele for par
        m /= 2
        cont += 1
    cont += n - m # caindo no primeiro caso de m < n, so com subtracao

print cont

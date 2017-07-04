n = input()

for i in range(n):
    pa = []
    # formando a parede de tijolos
    for i in range(9):
        if i % 2 == 0:
            pa.append(map(int, raw_input().split()))
        else:
            pa.append([0] * (i + 1))
    for i in range(0, 9, 2):
        if len(pa[i]) < i + 1:
            for j in range(i + 1):
                if j % 2 != 0:
                    pa[i].insert(j, 0)
    # resolvendo o problema
    for i in range(2, 9):
        if i % 2 == 0:
            for j in range(1, len(pa[i]), 2):
                z = pa[i][j]
                x = pa[i][j - 1]
                y = pa[i][j + 1]
                target = pa[i - 2][j - 1]
                z = (target - (x + y)) / 2
                pa[i][j] = z
                pa[i - 1][j - 1] = x + z
                pa[i - 1][j] = y + z
    for i in pa:
        for j in i:
            print j,
        print

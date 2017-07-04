def contaminate(matrix, x, y, n, m):
    if x > 0:
        if matrix[x-1][y] == 'A':
            matrix[x-1][y] = 'T'
            contaminate(matrix, x-1, y, n, m)
    if y > 0:
        if matrix[x][y-1] == 'A':
            matrix[x][y-1] = 'T'
            contaminate(matrix, x, y-1, n, m)
    if x < n-1:
        if matrix[x+1][y] == 'A':
            matrix[x+1][y] = 'T'
            contaminate(matrix, x+1, y, n, m)
    if y < m-1:
        if matrix[x][y+1] == 'A':
            matrix[x][y+1] = 'T'
            contaminate(matrix, x, y+1, n, m)

while True:
    n, m = map(int, raw_input().split())
    # n: altura da matriz
    # m: largura da matriz

    if n == 0 and m == 0:
        break

    water_tank = []
    for i in xrange(n):
        l = raw_input()
        # l: linha do water_tank
        water_tank.append(list(l))

    for i in xrange(n):
        for j in xrange(m):
            if water_tank[i][j] == 'T':
                contaminate(water_tank, i, j, n, m)

    for linha in water_tank:
        print ''.join(linha)
    print ""

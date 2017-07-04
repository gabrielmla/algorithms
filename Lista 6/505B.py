n, m = map(int, raw_input().split())
# n: numero de vertices
# m: numero de arestas
matriz = [[[] for j in xrange(n + 1)] for i in xrange(n + 1)]
vis = []

for i in xrange(m):
	a, b, c = map(int, raw_input().split())
	if c not in matriz[a][b]:
		matriz[a][b].append(c)
		matriz[b][a].append(c)


def dfs(u, v, c):
	if u in vis: return False
	if u == v: 
		if c not in cores: cores.append(c)
	else: vis.append(u)
	for i in xrange(1, n + 1):
		if len(matriz[u][i]) > 0:
			if c in matriz[u][i]:
				dfs(i, v, c)
				
queries = input()
for i in xrange(queries):
	cores = []
	u, v = map(int, raw_input().split())
	for c in xrange(1, 101):
		vis = []
		dfs(u, v, c)
	print len(cores)

from Queue import Queue
INF = 1000

n, m = map(int, raw_input().split())
matriz = [[1 for j in xrange(n)] for i in xrange(n)]
dist = [INF for i in xrange(n)]

for i in xrange(m):
	i, j = map(int, raw_input().split())
	i -= 1
	j -= 1
	matriz[i][j] = 2
	matriz[j][i] = 2

def bfs(node, value):
	fila = Queue()
	fila.put(node)
	dist[node] = 0
	
	while not fila.empty():
		top = fila.get()
		for i in xrange(len(matriz[node])):
			edge = matriz[top][i]
			if edge !=  value and dist[top] + 1 < dist[i]:
				fila.put(i)
				dist[i] = dist[top] + 1

bfs(0, matriz[0][n-1])
if dist[n-1] != INF:
	print dist[n-1]
else:
	print -1

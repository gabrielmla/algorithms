from Queue import PriorityQueue
n, m = map(int, raw_input().split())
graph = [[0 for j in xrange(n+1)] for i in xrange(n+1)]
INF = -1
dist = [INF for i in xrange(n)]


for i in xrange(m):
	a, b, c = map(int, raw_input().split())
	if graph[a][b] == 0 or graph[a][b] > c:
		graph[a][b] = c
		graph[b][a] = c

print graph

def bfs(grafo):
	fila = PriorityQueue()
	fila.put((0,1))
	dist[1] = 0
	
	while not fila.empty():
		node = fila.get()
		top = node[1]
		dis = node[0] * -1
		
		if dis == dist[top]:
			for i in xrange(len(dist[top])):
				node = grafo[top][i][0]
				wei = grafo[top][i][1]
				if dist[node] == INF or dist[node] > dis + wei:
					dist[node] = dis + wei
					fila.put((dist[node] * -1, node))
					
print dist

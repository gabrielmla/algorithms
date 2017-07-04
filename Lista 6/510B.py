import sys
sys.setrecursionlimit(10000)
 
n, m = map(int, raw_input().split())
 
matriz = []
for i in xrange(n):
	matriz.append(raw_input())
 
vis = [[0 for i in xrange(m)] for j in xrange(n)]
 
def validate(i, j, auxI, auxJ):
	if i >= n or j >= m or i < 0 or j < 0: 
		return False
	if matriz[i][j] != matriz[auxI][auxJ]: 
		return False
	return i != auxI or j != auxJ
 
def dfs(i, j, parI, parJ):
 
	if vis[i][j]:
		return True
 
	vis[i][j] = 1
 
	if validate(i+1, j, parI, parJ) and dfs(i+1, j, i, j):
		return True
	if validate(i-1, j, parI, parJ) and dfs(i-1, j, i, j):
		return True
	if validate(i, j+1, parI, parJ) and dfs(i, j+1, i, j):
		return True
	if validate(i, j-1, parI, parJ) and dfs(i, j-1, i, j):
		return True
 
	return False
 
flag = False
for i in xrange(n):
	for j in xrange(m):
		if not vis[i][j]:
			if dfs(i, j, i, j):
				print 'Yes'
				flag = True
				break
	if flag:
		break

if not flag:
	print 'No'

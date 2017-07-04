from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
n = input()
mah = []
vis = [0] * n
total = 0
size = 0
tempVis = [0] * n

def dfs(i, dic):
	for node in dic[i]:
		if vis[node] == 0:
			vis[node] = 1
			global size
			size += 1
			tempVis[node] = 1
			dfs(node, dic)

for i in xrange(n):
	mah.append(list(raw_input()))
	
cone = defaultdict(list)
for i in xrange(n):
	cone[i] = []
	
for j in xrange(n):
	for i in xrange(n):
		if i != j:
			if mah[j][i] == 'S':
				cone[j].append(i)

con_comp = 0
casas = []
comps = []
for node in cone:
	if vis[node] == 0:
		vis[node] = 1
		tempVis[node] = 1
		size += 1
		con_comp += 1
		dfs(node, cone)
		comps.append((list(tempVis), size))
		casas.append(size)
	tempVis = [0] * n
	size = 0

def isComplete(g, n, sN):
	cVertice = False
	
	nArestaVertice = []
	for i in xrange(sN):
		if g[i] == 1:
			size = len(cone[i])
			nArestaVertice.append(True if size == n - 1 else False)
	
	if (nArestaVertice[1:] == nArestaVertice[:-1]) and nArestaVertice[0] == True:
		cVertice = True
	
	return cVertice

for comp, ver in comps:
	if isComplete(comp, ver, n):
		total += 1

if total == len(comps):
	print len(comps)
	for i in casas:
		print i,
else:
	print -1

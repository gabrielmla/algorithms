q = input()
handles = {}

for i in xrange(q):
	old, new = raw_input().split()
	
	if not handles.has_key(old):
		# se nao foi requisitado essa handle
		handles[new] = old
	else:
		# as trocas
		handles[new] = handles[old]
		handles.pop(old)

print len(handles.items())

for h in handles:
	# imprimindo na msm linha
	print handles[h],
	print h

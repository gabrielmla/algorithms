n, m, k = map(int, raw_input().split())

seconds, mana = map(int, raw_input().split())

haste = map(int, raw_input().split())
hasteMana = map(int, raw_input().split())

insta = map(int, raw_input().split())
instaMana = map(int, raw_input().split())

if k > 0:
	canUse = 0
	spell = 0
	changed = False
	for s in xrange(k):
		if instaMana[s] > canUse and instaMana[s] <= mana:
			canUse = instaMana[s]
			spell = s
			changed = True
	mana -= canUse
	if changed == True:
		n -= insta[spell]

timeSpent = n * seconds
print timeSpent

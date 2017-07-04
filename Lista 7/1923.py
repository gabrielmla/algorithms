from collections import defaultdict


def anotherOne(name, l):
    if l[0] == name:
        return 1
    else:
        return 0


n, g = map(int, raw_input().split())
relations = []
amigos = []
amizade = {}
amizade = defaultdict(lambda: [], amizade)

for i in xrange(n):
    relations.append(raw_input().split())

def findRelations(rela):
	for r in rela:
		if "Rerisson" in r:
			outro = r[anotherOne("Rerisson", r)]
			amizade[0].append(outro)
			if outro not in amigos:
				amigos.append(outro)
		else:
			for j in xrange(g - 1):
				if r[0] in amizade[j] and r[1] not in amizade[j + 1]:
					if r[1] not in amigos:
						amigos.append(r[1])
					amizade[j + 1].append(r[1])
				elif r[1] in amizade[j] and r[0] not in amizade[j + 1]:
					if r[0] not in amigos:
						amigos.append(r[0])
					amizade[j + 1].append(r[0])
                
findRelations(relations)
relations = reversed(relations)
findRelations(relations)

amigos = sorted(amigos)
print len(amigos)
for a in amigos:
    print a

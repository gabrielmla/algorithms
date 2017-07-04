def dec_to_bra(string):
	top = ""
	mid = ""
	bot = ""
	for d in string:
		#top
		if d in "3467":
			top += "** "
		elif d in "1258":
			top += "*. "
		elif d in "90":
			top += ".* "
		#mid
		if d in "780":
			mid += "** "
		elif d in "45":
			mid += ".* "
		elif d in "269":
			mid += "*. "
		elif d in "13":
			mid += ".. "
		bot += ".. "

	print top[:-1]
	print mid[:-1]
	print bot[:-1]

def bra_to_dec(list, n):
	decimal = ""
	for i in xrange(n):
		if list[0][i] == "**":
			if list[1][i] == "..":
				decimal += "3"
			elif list[1][i] == ".*":
				decimal += "4"
			elif list[1][i] == "*.":
				decimal += "6"
			else:
				decimal += "7"
		elif list[0][i] == "*.":
			if list[1][i] == "..":
				decimal += "1"
			elif list[1][i] == "*.":
				decimal += "2"
			elif list[1][i] == ".*":
				decimal += "5"
			else:
				decimal += "8"
		elif list[0][i] == ".*":
			if list[1][i] == "*.":
				decimal += "9"
			elif list[1][i] == "**":
				decimal += "0"
	print decimal



while True:
	n = input()
	dec = ""
	bra = []
	if n == 0:
		break
		
	cmd = raw_input()
	
	if cmd == 'S':
		dec = raw_input()
		dec_to_bra(dec)
	elif cmd == 'B':
		for i in xrange(3):
			bra.append(raw_input().split())
		bra_to_dec(bra, n)

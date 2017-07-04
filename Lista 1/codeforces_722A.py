format = input()
hour = raw_input()
hora = int(hour[0] + hour[1])
minuto = int(hour[3] + hour[4])
hora_cor = hour[0] + hour[1]
min_cor = hour[3] + hour[4]

if format == 24:
	if hora > 23:
		hora_cor = "0" +  hour[1]
	if minuto > 59:
		min_cor = "0" + hour[4]
elif format == 12:
	if hora > 12 or hora == 0:
		if hora % 10 == 0:
			hora_cor = "10"
		else:
			hora_cor = "0" + hour[1]
	if minuto > 59:
		min_cor = "0" + hour[4]

correcao = ""
correcao += hora_cor + ":" + min_cor

print correcao
	

import csv, json

salas, sala_aux, sala_aux2 = [], '', []

#Adicionar baixo o nome do arquivo a ser convertido, considerando que esteja no mesmo diretório

with open('salas-sinternet.csv', 'r') as csvfile: 
	salas_lista = csv.reader(csvfile)
	for sala in salas_lista:
		salas.append(sala)
		if sala[0] == 'Sem':
			salas.remove(salas[salas.index(sala)])
		elif sala[10] != '':
			sala_aux = sala[10]
			sala_aux2.append({'Semestre': sala[0], 'Disciplina': sala[1], 'Professor': sala[2], 'Curso': sala[3], 'Código': sala[4], 'Dia': sala[5], 'Horário Inicial': sala[6], 'Horário Final': sala[7], 'Lab': sala[8], 'Compartilhada': sala[9], 'Sala': sala[10]})
		else:
			sala[10] = sala_aux
			sala_aux2.append({'Semestre': sala[0], 'Disciplina': sala[1], 'Professor': sala[2], 'Curso': sala[3], 'Código': sala[4], 'Dia': sala[5], 'Horário Inicial': sala[6], 'Horário Final': sala[7], 'Lab': sala[8], 'Compartilhada': sala[9], 'Sala': sala[10]})
		
	print(json.dumps(sala_aux2))
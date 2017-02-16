import csv, json

salas, sala_aux, sala_aux2 = [], '', []

for arquivo in range(1,11):
	arq = str(arquivo) + '.csv'
	with open(arq, 'r') as csvfile: 
		salas_lista = csv.reader(csvfile)
		for sala in salas_lista:
			salas.append(sala)
			if sala[0] == 'Sem':
				salas.remove(salas[salas.index(sala)])
			elif sala[10] != '':
				sala_aux = sala[10]
				sala_aux2.append({'sem': sala[0], 'dis': sala[1], 'prof': sala[2], 'curso': sala[3], 'codTurma': sala[4], 'dia': sala[5], 'hInicio': sala[6], 'hFim': sala[7], 'lab': sala[8], 'comp': sala[9], 'sala': sala[10]})
			else:
				sala[10] = sala_aux
				sala_aux2.append({'sem': sala[0], 'dis': sala[1], 'prof': sala[2], 'curso': sala[3], 'codTurma': sala[4], 'dia': sala[5], 'hInicio': sala[6], 'hFim': sala[7], 'lab': sala[8], 'comp': sala[9], 'sala': sala[10]})
			
	print(json.dumps(sala_aux2))

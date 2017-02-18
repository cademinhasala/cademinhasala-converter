import csv, json

salas, sala_aux, sala_aux2= [], '', [] 

arq2 = open('classes2.txt', 'w')

#Adicionar baixo o nome do arquivo a ser convertido, considerando que esteja no mesmo diretório

with open('9.csv', 'r') as csvfile: 
	salas_lista = csv.reader(csvfile)
	for sala in salas_lista:
		salas.append(sala)
		if sala[0] == 'Sem':
			salas.remove(salas[salas.index(sala)])
		else: 
			if sala[10] != '':
				sala_aux = sala[10]
				sala_aux2.append({'sem': sala[0], 'dis': sala[1], 'prof': sala[2], 'curso': sala[3], 'codTurma': sala[4], 'dia': sala[5], 'hInicio': sala[6], 'hFim': sala[7], 'lab': sala[8], 'comp': sala[9], 'sala': sala[10]})
			else:
				sala[10] = sala_aux
				sala_aux2.append({'sem': sala[0], 'dis': sala[1], 'prof': sala[2], 'curso': sala[3], 'codTurma': sala[4], 'dia': sala[5], 'hInicio': sala[6], 'hFim': sala[7], 'lab': sala[8], 'comp': sala[9], 'sala': sala[10]})
			
arq2.write(json.dumps(sala_aux2))
arq2.close()

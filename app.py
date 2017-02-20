import csv, json

salas, sala_aux, sala_aux2= [], '', [] 

arq2 = open('classes2-ts.txt', 'w')

#Adicionar baixo o nome do arquivo a ser convertido, considerando que esteja no mesmo diretório

with open('12.csv', 'r') as csvfile: 
	salas_lista = csv.reader(csvfile)
	for sala in salas_lista:
		salas.append(sala)
		if sala[0] == 'Sem':
			salas.remove(salas[salas.index(sala)])
		else: 
			if sala[10] != '':
				sala_aux = sala[10]
				sala_aux2.append({'sem': sala[0].strip(), 'dis': sala[1].strip(), 'prof': sala[2].strip(), 'curso': sala[3].strip(), 'codTurma': sala[4].strip(), 'dia': sala[5].strip(), 'hInicio': sala[6].strip(), 'hFim': sala[7].strip(), 'lab': sala[8].strip(), 'comp': sala[9].strip(), 'sala': sala[10].strip()})
			else:
				sala[10] = sala_aux
				sala_aux2.append({'sem': sala[0].strip(), 'dis': sala[1].strip(), 'prof': sala[2].strip(), 'curso': sala[3].strip(), 'codTurma': sala[4].strip(), 'dia': sala[5].strip(), 'hInicio': sala[6].strip(), 'hFim': sala[7].strip(), 'lab': sala[8].strip(), 'comp': sala[9].strip(), 'sala': sala[10].strip()})
			
arq2.write(json.dumps(sala_aux2))
arq2.close()

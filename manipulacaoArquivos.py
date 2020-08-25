#neste arquivo estão todas as funções que manipulam os arquivos

def getArquivoMedicamentos():
	f=open('medicamento.text', 'r')
	lista=[]
	for linha in f:
		dados=linha.split()
		medicamento=[]
		medicamento.append(int(dados[0]))
		dados[1]=list(dados[1])
		for j in range(len(dados[1])):
			if dados[1][j]=='%':
				dados[1].pop(j)
				dados[1].insert(j,' ')
		dados[1] = ''.join(str(i) for i in dados[1])
		medicamento.append(str(dados[1]))
		dados[2]=list(dados[2])
		for j in range(len(dados[2])):
			if dados[2][j]=='%':
				dados[2].pop(j)
				dados[2].insert(j,' ')
		dados[2] = ''.join(str(i) for i in dados[2])
		medicamento.append(str(dados[2]))
		medicamento.append(float(dados[3]))
		medicamento.append(int(dados[4]))
		medicamento.append(int(dados[5]))
		lista.append(medicamento)
	f.close
	return lista
	
def getArquivoFabricantes():
	lista=[]
	f=open('fabricantes.text', 'r')
	for linha in f:
		dados=linha.split()
		dados[0]=int(dados[0])
		dados[1]=list(dados[1])
		for j in range(len(dados[1])):
			if dados[1][j]=='%':
				dados[1].pop(j)
				dados[1].insert(j,' ')
		dados[1] = ''.join(str(i) for i in dados[1])
		lista.append(dados)
	f.close
	return lista

def atualizaArquivoFabricantes(lista):
	f=open('fabricantes.text', 'w')
	for i in range(len(lista)):
		f.write(str(lista[i][0]))
		f.write("\t")
		lista[i][1]=list(lista[i][1])
		for j in range(len(lista[i][1])):
			if lista[i][1][j]==' ':
				lista[i][1].pop(j)
				lista[i][1].insert(j,'%')
		lista[i][1] = ''.join(str(e) for e in lista[i][1])
		f.write(str(lista[i][1]))#nome
		f.write("\n")
	f.close

def atualizaArquivoMedicamentos(lista):
	f=open('medicamento.text', 'w')
	for i in range(len(lista)):
		remedio=lista[i]
		f.write(str(remedio[0]))#codigo
		f.write("\t")
		
		remedio[1]=list(remedio[1])
		for j in range(len(remedio[1])):
			if remedio[1][j]==' ':
				remedio[1].pop(j)
				remedio[1].insert(j,'%')
		remedio[1] = ''.join(str(i) for i in remedio[1])
		f.write(str(remedio[1]))#nome
		f.write("\t")
		
		remedio[2]=list(remedio[2])
		for j in range(len(remedio[2])):
			if remedio[2][j]==' ':
				remedio[2].pop(j)
				remedio[2].insert(j,'%')
		remedio[2] = ''.join(str(i) for i in remedio[2])
		f.write(str(remedio[2]))
		f.write("\t")
			
		for j in range(3,len(remedio)):
			f.write(str(remedio[j]))
			f.write("\t")
		f.write("\n")
	f.close
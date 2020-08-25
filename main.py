from manipulacaoArquivos import*

def imprimeRemedio(remedio):
	print ('Código:\t\t\t\t', remedio[0])
	print ('Nome:\t\t\t\t', remedio[1])
	print ('Princípio Ativo:\t', remedio[2])
	print ('Preço Unitário:\t\t', remedio[3])
	print ('Quantidade:\t\t\t', remedio[4])
	print ('Código Fabricante:\t', remedio[5])
	print("\n")

def imprimeEstoque(lista):
	for remedio in lista:
		imprimeRemedio(remedio)

def filtraPorCodigo(lista):
	try:
		codigo=int(input("Qual código deseja buscar?"))
	except:
		print('Valor inserido não válido')
		print('Retornando ao menu principal')
		return
	encontrou=False
	print()
	for remedio in lista:
		if remedio[0]==codigo:
			imprimeRemedio(remedio)
			encontrou=True
	if encontrou==False:
		print("Nenhum remedio encontrado")

def filtraPorPreco(lista):
	try:
		a=float(input('Insira o valor minimo:'))
	except:
		print('Valor inseiro não válido')
		print('Retornando ao menu principal\n')
		return
	try:
		maior=float(input('Insira o valor maximo:'))
	except:
		print('Valor inseiro não válido')
		print('Retornando ao menu principal\n')
		return
	menor=min(a,maior)
	maior=max(a,maior)
	for remedio in lista:
		if remedio[3]>=menor and remedio[3]<=maior:
			imprimeRemedio(remedio)

def filtraPorCodigoFabricante(lista):
	try:
		a=int(input("Digite o Código do fabricante:"))
		print()
	except:
		print('Código de fabricante deve ser um numero inteiro.')
		print('Retornando ao menu principal\n')
		return
	for remedio in lista:
		if a == remedio[5]:
			imprimeRemedio(remedio)

def fazVenda():
	venda=[]
	try:
		c=int(input('Insira  código do medicamento a ser vendido:'))
	except:
		print('\nCódigo de fabricante deve ser um numero inteiro.')
		print('Retornando ao menu principal\n')
		return
	venda=[c]
	encontrou=False
	for i in range(len(medicamentos)):
		remedio=list(medicamentos[i])
		if remedio[0]==c:
			print('Nome:', remedio[1])
			print('Preço Unitário:', remedio[3])
			print('Quantidade:', remedio[4])
			venda.append(remedio[1])
			venda.append(remedio[3])
			encontrou=True
			q=int(input('Quantidade a ser vendida:'))
			while q>remedio[4]:
				print('Valor superior a quantidade em estoque.')
				q=int(input('Quantidade a ser vendida:'))
			medicamentos[i][4]-=q
			if remedio[4]==0:
				medicamentos.pop(i)
			break
	if encontrou:
		novaVenda=True
		for x in vendaGeral:
			if x[0]==c:
				x[1]+=q
				novaVenda=False
		if novaVenda:
			venda.append(q)
			vendaGeral.append(venda.copy())
	else:
		print('Nenhum medicamento encontrado!')

def setFabricante():
	#INDICES DA LISTA FABRICANTES: 0 - codigo do fabricante(int>0)|1- nomeFabricante
	fabricante=[]
	print('Insira os dados do fabricante conforme solicitado.')
	codigo=-1
	while codigo<=0 :
		novamente=False
		try:
			codigo=int(input('1 - Código: '))
		except: 
			print('Código deve ser um número inteiro!')	
			print('Para tentar novamente digite --->SIM<---')
			print('Para retornar ao menu principal digite --->NÂO<---')
			novamente=input()
			if novamente.lower()=='sim':
				novamente == True
			else: 
				return False
		if codigo<=0:
			if novamente == False:
				print('Código não válido')
		else:
			for elemento in fabricantes:
				if elemento[0]==codigo:
					print('O fabricante já está cadastrado.')
					print('Para tentar novamente digite --->SIM<---')
					print('Para retornar ao menu principal digite --->NÂO<---')
					novamente=input()
					if novamente.lower()=='sim':
						imprimeFabricantes(fabricantes)
						return setFabricante()
					else:
						return False		
			fabricante.append(codigo)
			nome=(input('2 - Nome:'))
			fabricante.append(nome)
			return fabricante

def setMedicamento(): 
	#INDICES DA LISTA MEDICAMENTO: 0-codigo(int>0| 1-nome(string)|2-nomePrincipioAtivo(string)|3-precoUnitario(float>=0)|4-quantidade(int>=0)|codigoFrabricante(lista)
	print('Insira os dados do medicamento conforme solicitado.')
	medicamento=[]
	c=-1
	while c<0:
		c=int(input('1 - Código: '))
		if c<0:
			print('Código não válido')
		else:
			medicamento.append(c)
	nome=(input('2 - Nome:'))
	medicamento.append(nome)
	principioAtivo=(input('3 - Principio Ativo:'))
	medicamento.append(principioAtivo)
	precoUnitario=-1
	while precoUnitario<=0:
		precoUnitario=float(input("4 - Preço Unitário: "))
		if precoUnitario<=0:
			print('Preço Unitário não válido')
		else:		
			medicamento.append(precoUnitario)
	quantidade=-1
	while quantidade<0:
		quantidade=int(input("5 - Quantidade: "))
		if quantidade<=0:
			print('Quantidade não válida')
		else:		
			medicamento.append(quantidade)
	c=-1
	while c<0:
		cadastrado=False
		c=int(input('6 - Código do Fabricante: '))
		if c<0:
			print('Código não válido')
		for fabricante in fabricantes:
			if c==fabricante[0]: 
				cadastrado=True
		if cadastrado==False:
			return False
	medicamento.append(c)
	return medicamento

def removeMedicamento():
	c=0
	while c<1 or c>2:
		print('Escolha como remover o medicamento:')
		print('1-Remover por código do medicamento.')
		print('2-Remover por código da fabricante.')
		print('3-Retornar ao menu principal.')
		try:
			c=int(input("Digite o numero correspondente a opção desejada: "))
			if c<1 or c>3:
				print("Opção não válida")
		except:
			print("Digite o número correspondente a sua opção!")
			removeMedicamento()
			return	
	if c==1:
		try:
			c=int(input("Digite o código do medicamento: "))
		except:
			print("O código deve ser um número inteiro")
			return
		for i in range(len(medicamentos)):
			if medicamentos[i][0]==c:
				print('Medicamento "', medicamentos[i][1],'" removido')
				medicamentos.pop(i)
				return	
	elif c==2:
		try:
			c=int(input("Digite o código do fabricante: "))
		except:
			print("O código deve ser um número inteiro")
			return
		i=0
		while i<len(medicamentos):
			if medicamentos[i][5]==c:
				print('Medicamento "', medicamentos[i][1],'" removido')
				medicamentos.pop(i)
				i-=1
			i+=1
	elif c==3:
		return			
	else:
		print('Código não Válido')
		removeMedicamento()

def removeFabricantes():
	try:
		c=int(input('Insira o código do fabricante a ser removido:'))
		encontrou=False
		for i in range(len(fabricantes)):
			if c == fabricantes[i][0]:
				encontrou=True
				print('Fabricante', fabricantes[i][1], 'removido')
				fabricantes.pop(i)
				break
		for i in range(len(medicamentos)):
			if c == medicamentos[i][5]:
				encontrou=True
				print('Medicamento', medicamentos[i][1], 'removido')
				medicamentos.pop(i)
				i=-1
		if encontrou==False:
			print('Não foi encontrado nada a ser removido')
	except:
		print('O código digitado deve ser um número inteiro')
		
def imprimeFabricantes(lista):
	for i in range(len(lista)):
		print('Fabricante:', i+1)
		print ('Código:', lista[i][0])
		print ('Nome:', lista[i][1])
		print("\n")

def imprimeVendas():
	valorTotalVenda=0
	print('Relatório de Vendas')
	for venda in vendaGeral:
		print()
		print('Código:\t\t\t\t', venda[0])
		print('Nome:\t\t\t\t', venda[1])
		print('Preço Unitário:\t\t', venda[2])
		print('Quantidade da venda:', venda[3])
		c=venda[3]*venda[2]
		print('Valor da Venda:\t', c)
		valorTotalVenda+=c
	print()
	print('Valor total das vendas:', valorTotalVenda)

def imprimeOpcoes():
	print("GERENCIADOR DE ESTOQUE E VENDA DE MEDICAMENTOS")
	print("Selecione a opção desejada:")
	print('0 - ENCERRAR O PROGRAMA')
	print("1 - Apresentar estoque de medicamentos.")
	print("2 - Cadastrar novo medicamento.")
	print("3 - Remover medicamento do cadastro de medicamentos.")
	print("4 - Vender medicamento.")
	print("5 - Cadastrar novo fabricante.")
	print("6 - Remover fabricante do cadastro.")
	print("7 - Exibir fabricantes cadastrados.")
	print("8 - Exibir relatórios de venda.")

#MAIN
medicamentos=getArquivoMedicamentos()
fabricantes=getArquivoFabricantes()
vendaGeral=[]

while True:
	imprimeOpcoes()
	c=input("Digite o numero correspondete a opção desejada: ")
	if c=='1':#Apresentar estoque de medicamento
		c=0
		while True:
			print('Escolha como apresentar o estoque.')
			print('1-Apresentar todo estoque.')
			print('2-Filtrar por código.')
			print('3-Filtrar por preço.')
			print('4-Filtrar por código do fabricante.')
			c=input('Digite o numero respetivo a opção desejada:')
			print()
			if c=='1':
				imprimeEstoque(medicamentos)
				break
			elif c=='2':
				filtraPorCodigo(medicamentos)
				break
			elif c=='3':
				filtraPorPreco(medicamentos)
				break
			elif c=='4':#filtra por codigo do fabricante
				filtraPorCodigoFabricante(medicamentos)
				break
			else:
				print("Opção não válida")
				break

	elif c=='2':#cadastrar novo medicamento
		novoMedicamento=setMedicamento()
		if novoMedicamento==False:
			print('Fabricante não cadastrado')
			print('Cadastre este fabriante primeiro')
		else:
			medicamentos.append(novoMedicamento.copy())
	elif c=='3': #remover medicamento do cadastro
		removeMedicamento()
	elif c=='4': #vender medicamento
		fazVenda()
	elif c=='5': #cadastrar novo fabricante
		novoFabricante=setFabricante()
		if novoFabricante==False:
			print('Nenhum fabricante foi cadastrado!')
		else:
			fabricantes.append(novoFabricante.copy())
	elif c=='6':# remover fabricante do cadastro
		removeFabricantes()
	elif c=='7':#exibir fabricantes cadastrados
		imprimeFabricantes(fabricantes)
	elif c=='8': #exibir relatórios de venda
		imprimeVendas()
	elif c=='0':
		break
	else:
		print('\nOpção não válida\n')

print('Salvando dados')
atualizaArquivoMedicamentos(medicamentos)
atualizaArquivoFabricantes(fabricantes)
print('Programa encerrado com sucesso')
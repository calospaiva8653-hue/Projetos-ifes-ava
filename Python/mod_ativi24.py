def f_preencherTurma()->list:
	arquivo = open('pessoas.txt','r')
	alunos = list()
	dados = list()
	
	for linha in arquivo:
		dados = linha.split(";")
		dados[1]=int(dados[1])
		dados[2]=float(dados[2])
		dados[3]=float(dados[3])
		alunos.append(dados)
	
	arquivo.close()
	return alunos

def RelatorioOrdenadoNome23(listadeli:list):
	arquivo02=open('saida1.txt', 'w')
	listaOrdNome = list()
	listaOrdNome=listadeli.copy()
	listaOrdNome.sort(key=lambda x: x[0])
	for i in listaOrdNome:
		peso=i[2]
		altura=i[3]
		imc = peso/(altura**2)
		arquivo02.write(f"NOME={i[0]} IMC={imc:.2f}\n")
	arquivo02.close()
def RelatorioOrdenadoNome(listadeli:list):
	listaOrdNome = list()
	listaOrdNome=listadeli.copy()
	listaOrdNome.sort(key=lambda x: x[0])
	for i in listaOrdNome:
		peso=i[2]
		altura=i[3]
		imc = peso/(altura**2)
		print(f"NOME={i[0]} IMC={imc:.2f}")
	
def RelatorioOrdenadoIMC23(listadeli:list):
	arquivo03=open('saida2.txt', 'w')
	listaOrdIMC = list()
	listaOrdIMC = listadeli.copy()
	listaOrdIMC.sort(key=lambda x: x[2]/x[3]**2)
	for i in listaOrdIMC:
		nome=i[0]
		peso=i[2]
		altura=i[3]
		imc = peso/(altura**2)
		arquivo03.write(f"IMC={imc:.2f} NOME={nome}\n")
	arquivo03.close()
def RelatorioOrdenadoIMC(listadeli:list):
	listaOrdIMC = list()
	listaOrdIMC = listadeli.copy()
	listaOrdIMC.sort(key=lambda x: x[2]/x[3]**2)
	for i in listaOrdIMC:
		nome=i[0]
		peso=i[2]
		altura=i[3]
		imc = peso/(altura**2)
		print(f"IMC={imc:.2f} NOME={nome}")
	

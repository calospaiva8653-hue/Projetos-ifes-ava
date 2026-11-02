def f_preencherLista(n:int)->list:
	lista=list()
	nome = str()
	idade = int()
	peso = float()
	altura = float()
	listainterna = list()
	
	for i in range(n):
		lista=list()
	
		nome=input()
		lista.append(nome)
		idade=int(input())
		lista.append(idade)
		peso=float(input())
		lista.append(peso)
		altura=float(input())
		lista.append(altura)
		listainterna.append(lista)
		
	
	return listainterna
	
def CalcularIMC(listadeli:list):
	peso=float()
	altura=float()
	imc=float()
	conta=int()
    
	for i in listadeli:
		nome=i[0]
		altura=i[3]
		peso=i[2]
		
		imc=peso/altura**2
		
		print(f"NOME={nome} IMC={imc:.2f}")
    
	
	
def main():
	alunos = int()
	todos = list()
	
	alunos = int(input())
	
	todos=f_preencherLista(alunos)
	
	CalcularIMC(todos)
	
if __name__ == "__main__":
	main()
def f_preencheLista(n:int)->list:
	y=list()
	
	for i in range(n):  
		x=int(input())
		y.append(x)
	
	return y
	
	
def f_somaValorPosiPares(lista:list)->tuple:
	somaPos = int()
	somaPares = int()
	
	for i in range(len(lista)):
		num = lista[i]
		
		if(num % 2 == 0):
			somaPares+=num
		if(i % 2 == 0):
			somaPos+=num
		
	return somaPos,somaPares
	
def f_somaValorPosiImpares(lista:list)->tuple:
	somaPos = int()
	somaImpares = int()
	
	for i in range(len(lista)):
		num = lista[i]
		
		if(num % 2 != 0):
			somaImpares+=num
			
		if(i % 2 != 0):
			somaPos+=num
		
	return somaPos,somaImpares
	
def f_imprimeLista(lista:list):
	
	for i in range(len(lista)):
		print(f'LISTA[{i}]={lista[i]}')
		
	
def main():
	# declaração
	n=int()
	lista=list()
	imparesValores = int()
	imparesPos = int()
	paresValores = int()
	paresPos = int()
	
	# entrada
	n=int(input())
	
	# processamento
	lista = f_preencheLista(n)
	imparesPos, imparesValores = f_somaValorPosiImpares(lista)
	paresPos, paresValores = f_somaValorPosiPares(lista)
	# saída
	print(f"TODOS")
	f_imprimeLista(lista)
	print(f"SOMA PARES={paresValores}")
	print(f"SOMA DOS ELEMENTOS DAS POSICOES PARES={paresPos}")
	print(f"SOMA IMPARES={imparesValores}")
	print(f"SOMA DOS ELEMENTOS DAS POSICOES IMPARES={imparesPos}")
	
if __name__ == "__main__":
    main()
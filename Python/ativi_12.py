def f_preencheLista(n:int)->list:
	y=list()
	
	for i in range(n):  
		x=float(input())
		y.append(x)
	
	return y
	
def f_separaParImpar(a:list)->tuple:
	impar=list()
	par=list()
	for i in a:
		if(i%2==0):
			par.append(i)
		else:
			impar.append(i)
	return par,impar

def f_imprimeLista(a2:list):
	
	for i in range(len(a2)):
		print(f'LISTA[{i}]={a2[i]:.0f}')
		
	
def main():
	#declaração de variáveis
	n = int()
	normal= list()
	tres= list()
	par2= list()
	impar2= list()

	#entrada de dados
	n=int(input())

	#processamento
	normal=f_preencheLista(n)
	tres=f_separaParImpar(normal)
	par2=tres[0]
	impar2=tres[1]

	#saída de dados
	
	print(f"TODOS")
	f_imprimeLista(normal)
	print(f"PARES")
	f_imprimeLista(par2)
	print(f"IMPARES")
	f_imprimeLista(impar2)
    
if __name__ == "__main__":
    main()

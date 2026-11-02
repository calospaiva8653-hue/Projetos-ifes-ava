def f_preencheLista(n:int)->list:
	y=list()
	
	for i in range(n):  
		x=float(input())
		y.append(x)
	
	return y
	
def f_somaLista(lista:list)->float:
	soma=float()
	
	for i in range(len(lista)):
		soma+=lista[i]
	
	return soma

def f_imprimeLista(lst_numeros:list):
	cre= lst_numeros[:]
	cre.sort()
	for i in range(len(cre)):
		print(f'LISTA[{i}]={cre[i]:.2f}')
	
def main():
	
    #declaração de variáveis
    lst_numeros = list()
    n = int()
    soma = float()
    
    #Entrada de dados
    n = int(input())
    
    #Processamento
    lst_numeros = f_preencheLista(n)
    soma = f_somaLista(lst_numeros)
    
    #Saída
    f_imprimeLista(lst_numeros)
    print(f"Soma total={soma:.2f}")

if __name__ == "__main__":
    main()
    
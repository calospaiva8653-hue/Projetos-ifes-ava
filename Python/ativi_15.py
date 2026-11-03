def f_preencherLista(n:int)->list:
	y=list()
	
	for i in range(n):  
		x=float(input())
		y.append(x)
	
	return y
	
def f_calculaMediaPonderada(lista1:list, lista2:list)->float:
	soma=0
	soma2 = 0
	l1 = float()
	l2 = float()
	for i in range(len(lista1)):
		l1 = lista1[i]
		l2 = lista2[i]
		produto=l1 * l2
		soma+=produto
		soma2+=lista2[i]
	mp=soma/soma2
    
	return mp
    
def f_imprimeLista(lista:list,matricula:str):
	
	for i in range(len(lista)):
		print(f'MATRICULA={matricula} MEDIA PONDERADA={lista}')
		
def main():
	#declaração
	numeroavali=int()
	pesos = list()
	media = list()
	somatotal= float
	cons = int
	menor=float
	maior=float
	mediatotal = float()
	cons=1
	somatotal = 0.0
	menor = 0.0
	maior = 0.0
    
	#entrada
	numeroavali=int(input())
	matricula=str(input())
	pesos= f_preencherLista(numeroavali)
    
	#processo
	while(matricula!="FIM"):
		notas=f_preencherLista(numeroavali)
		media=f_calculaMediaPonderada(pesos , notas)
		if(cons==1):
			maior = media
			menor = media
		elif (media > maior):
			maior = media
		elif (media < menor):
			menor = media
		somatotal+=media
		f_imprimeLista(media , matricula)
		matricula=str(input())
		cons+=1
		
	mediatotal = somatotal / (cons - 1)
	print(f"MEDIA TURMA={mediatotal}")
	print(f"MAIOR MEDIA PONDERADA={maior}")
	print(f"MENOR MEDIA PONDERADA={menor}")
		
	
if __name__ "__main__":
	main()
    
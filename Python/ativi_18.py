def f_preencherLista(n:int)->list:
	y=list()
	x=str()
	
	while len(y)< n:
		x=str(input()).upper()
		
		if x not in y:
			y.append(x)
	
	return y

def f_imprimeLista(comp1:list,comp2:list):
	conta=int()
	conta=1
	
	for i in range(len(comp1)):
		
		for j in range(len(comp2)):
			print(f"JOGO {conta} – {comp1[i]} x {comp2[j]}")
			conta+=1
		
		
		
def main():
	nu01=int()
	nu02=int()
	comp1=list()
	comp2=list()
    
    
	nu01=int(input())
	nu02=int(input())
    
	comp1=f_preencherLista(nu01)
	comp2=f_preencherLista(nu02)
    
	f_imprimeLista(comp1,comp2)
	f_imprimeLista(comp2,comp1)

    
if __name__ == "__main__":
	main()

import mod_ativi24
def main():
	todos = list()
	
	todos=mod_ativi24.f_preencherTurma()
	mod_ativi24.RelatorioOrdenadoNome(todos)
	mod_ativi24.RelatorioOrdenadoIMC(todos)
	mod_ativi24.RelatorioOrdenadoNome23(todos)
	mod_ativi24.RelatorioOrdenadoIMC23(todos)
	
if __name__ == "__main__":
	main()

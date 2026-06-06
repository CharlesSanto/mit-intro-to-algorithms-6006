def encontrar_aniversario_repetido(turma):
    
    registro = set()
    
    for aniversario in turma:
        
        if aniversario in registro:
            return aniversario
        
        registro.add(aniversario)
        
    return "Nenhum par encontrado"
    
turma_teste = ["22-11", "22-11", "03-01", "15-05", "30-12"]
resultado = encontrar_aniversario_repetido(turma_teste)
print(f"Resultado da busca {resultado}")
    
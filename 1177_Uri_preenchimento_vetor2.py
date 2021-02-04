def main():
    
    valor = int(input("Qual valor: "))
    vetor = []
    elemento = 0
    contador = 0
    
    while contador <(1000):
        vetor.append(elemento)
        print(f"N[{contador}] = {elemento}")
        if elemento < (valor-1):
            elemento += 1
        
        else:
            elemento == valor-1
            elemento = 0
        
        contador += 1
        

if __name__=="__main__":
    main()
def main():
    entrada = input("Indique dois valores inteiros: ")
    dados = entrada.split()
    x = int(dados[0])
    y = int(dados[1])

    while not x == y:
        if x > y:
            print("Decrescente")
        
        else:
            print("Crescente")
        entrada = input("Indique outros dois valores inteiros: ")
        dados = entrada.split()
        x = int(dados[0])
        y = int(dados[1])

if __name__=="__main__":
    main()
def main():
    n = (input("Dois valores: "))
    dados = n.split()
    qtd_numeros = int(dados[0])
    limite_sup = int(dados[1])
    contador = 1

    for i in range(1, int((limite_sup/qtd_numeros)) + 1):
        print(" ")
        for c in range(1, qtd_numeros+1):
            print(f"{contador}", end=" ")
            contador += 1
    
if __name__=="__main__":
    main()
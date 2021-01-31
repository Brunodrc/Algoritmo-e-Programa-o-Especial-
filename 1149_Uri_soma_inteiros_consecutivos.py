def main():

    entrada = input("quais valores: ")
    dados = entrada.split()
    a = int(dados[0])
    limite_sup = len(dados) - 1
    n = int(dados[limite_sup])

    soma = 0 

    for i in range(0, n):
        soma += a + i
    
    print(soma)

if __name__=="__main__":
    main()
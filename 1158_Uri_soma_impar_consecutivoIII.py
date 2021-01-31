def main():
    testes = int(input("Quantos testes: "))

    for i in range(testes):
        
        linha = input("Indique X e Y: ")
        dados = linha.split()
        x = int(dados[0])
        y = int(dados[1])
        soma = 0
        contador = 1

        while contador <= y:
            if x % 2 != 0:
                soma += x
                x += 1
                contador += 1
            else:
                x += 1
        print(soma)


if __name__=="__main__":
    main()
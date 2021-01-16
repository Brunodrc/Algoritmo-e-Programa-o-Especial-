def main():
    entrada = input("Valores: ")

    dados = entrada.split()
    valor1 = int(dados[0])
    valor2 = int(dados[1])
    valor3 = int(dados[2])

    if valor1 < valor2 and valor1 < valor3:
        A = valor1
        if valor2 < valor3:
            B = valor2
            C = valor3
        else:
            B = valor3
            C = valor2
    elif valor2 < valor1 and valor2 < valor3:
        A = valor2
        if valor1 < valor3:
            B = valor1
            C = valor3
        else:
            B = valor3
            C = valor1
    elif valor3 < valor1 and valor3 < valor2:
        A = valor3
        if valor1 < valor2:
            B = valor1
            C = valor2
        else:
            B = valor2 
            C = valor1
    
    print(A)
    print(B)
    print(C)
    print(" ")
    print(dados[0])
    print(dados[1])
    print(dados[2])


if __name__ == "__main__":
    main()
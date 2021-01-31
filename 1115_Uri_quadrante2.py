def main():
    entrada = input("Digite as coordenadas do ponto: ")

    dados = entrada.split()
    x = float(dados[0])
    y = float(dados[1])

    while not x == 0 or y == 0:

        if x > 0 and y > 0:
            print("primeiro")
        elif x < 0 and y > 0:
            print("segundo")
        elif x < 0 and y < 0:
            print("terceiro")
        elif y < 0:
            print("quarto")
        
        entrada = input("Digite as coordenadas do ponto: ")
        dados = entrada.split()
        x = float(dados[0])
        y = float(dados[1])

if __name__=="__main__":
    main()
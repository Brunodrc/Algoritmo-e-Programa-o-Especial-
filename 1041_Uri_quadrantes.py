def main():
    entrada = input("Digite as coordenadas do ponto: ")

    dados = entrada.split()
    x = float(dados[0])
    y = float(dados[1])

    if x == y and x == 0:
        print("Origem")
    elif x == 0:
        print("Eixo Y")
    elif y == 0:
        print("Eixo X")
    elif x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    elif y < 0:
        print("Q4")

if __name__ == "__main__":
    main()
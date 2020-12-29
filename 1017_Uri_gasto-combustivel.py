def main():
    # entrada
    horas = int(input("Digite as horas: "))
    velocidade_media = int(input("Digite a velociade média me km/h: "))

    #processamento
    gasto = (velocidade_media * horas) / 12

    # saida
    print(f"{gasto:.3f}")

main()

def main():
    entrada = input("Insira as quatro notas: ")

    dados = entrada.split()
    N1 = float(dados[0])
    N2 = float(dados[1])
    N3 = float(dados[2])
    N4 = float(dados[3])

    media_p = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / (2 + 3 + 4 + 1)

    if media_p >= 7:
        print(f"Média: {media_p:.1f}")
        print("Alun@ aprovad@")
    elif media_p < 5:
        print(f"Média: {media_p:.1f}")
        print("Alun@ reprovad@")
    elif media_p >= 5 and media_p <= 6.9:
        print(f"Média: {media_p:.1f}")
        print("Alun@ em exame")
        exame_final = float(input("Digite a nota do exame final: "))
        nova_media = (media_p + exame_final) / 2
        if nova_media >= 5.0:
            print("Alun@ aprovad@")
            print(f"Média: {nova_media:.1f}")
        else:
            print(f"Média: {nova_media:.1f}")
            print("Alun@ reprovad@")

if __name__ == "__main__":
    main()
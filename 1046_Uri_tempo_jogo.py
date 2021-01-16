def main():
    entrada = input("Digite a hora inicial e a hora final: ")

    dados = entrada.split()
    hora_inicial = int(dados[0])
    hora_final = int(dados[1])

    if hora_inicial == hora_final:
        print("O JOGO DUROU 24 HORA(S)")
    else:
        if hora_inicial >= 12:
            total = 24 - abs(hora_final - hora_inicial)
        else:
            total = hora_final - hora_inicial

        print(f"O JOGO DUROU {total} HORA(S)")

if __name__ == "__main__":
    main()
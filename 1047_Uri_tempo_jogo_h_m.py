def main():
    entrada = input("Digite hora inicial, minuto inicial, hora final e minuto final: ")

    dados = entrada.split()
    hora_inicial = int(dados[0])
    minuto_inicial = int(dados[1])
    hora_fim = int(dados[2])
    minuto_fim = int(dados[3])

    hora_total = hora_fim - hora_inicial

    if hora_total < 0:
        hora_total += 24
    
    minuto_total = minuto_fim - minuto_inicial

    if minuto_total < 0:
        minuto_total += 60
        hora_total -= 1

    if hora_fim == hora_inicial and minuto_fim == minuto_inicial:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else:
        print(f"O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)") 


if __name__ == "__main__":
    main()
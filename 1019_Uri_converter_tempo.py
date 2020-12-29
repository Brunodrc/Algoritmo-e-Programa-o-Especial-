def main():
    # entrada
    tempo_segundos = int(input("Digite os segundos: "))

    #processamento
    horas = tempo_segundos // 3600
    resto = tempo_segundos % 3600

    minutos = resto // 60
    resto = minutos % 60

    segundos = tempo_segundos % 60

    #saida
    print(f"{horas}:{minutos}:{segundos}")

main()

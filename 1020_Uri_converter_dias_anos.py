def main():
    #entrada
    dias = int(input("Dias: "))

    #processamento
    anos = dias // 365
    resto = dias % 365

    meses = resto // 30
    resto = resto % 30

    dias = resto

    #saida
    print(f"{anos} ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)")

main()

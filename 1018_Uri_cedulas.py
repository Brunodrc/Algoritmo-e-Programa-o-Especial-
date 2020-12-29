def main():
    # entrada
    valor = int(input("Digite um valor: "))

    #processamento
    cedula_100 = valor // 100
    resto_100 = valor % 100

    cedula_50 = resto_100 // 50
    resto_50 = resto_100 % 50

    cedula_20 = resto_50 // 20
    resto_20 = resto_50 % 20

    cedula_10 = resto_20 // 10
    resto_10 = resto_20 % 10

    cedula_5 = resto_10 // 5
    resto_5 = resto_10 % 5

    cedula_2 = resto_5 // 2
    resto_2 = resto_5 % 2

    cedula_1 = resto_2

    #saida
    print(valor)
    print(f"{cedula_100} nota(s) de R$ 100,00")
    print(f"{cedula_50} nota(s) de R$ 50,00")
    print(f"{cedula_20} nota(s) de R$ 20,00")
    print(f"{cedula_10} nota(s) de R$ 10,00")
    print(f"{cedula_5} nota(s) de R$ 5,00")
    print(f"{cedula_2} nota(s) de R$ 2,00")
    print(f"{cedula_1} nota(s) de R$ 1,00")

main()

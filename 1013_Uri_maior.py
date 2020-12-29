def main():
    #entrada
    numeros = input("Digite 3 números: ")
    desempacotar = numeros.split()
    A = int(desempacotar[0])
    B = int(desempacotar[1])
    C = int(desempacotar[2])

    #processamento
    Maior_AB = (A + B + abs(A - B)) / 2
    Maior_ABC = (Maior_AB + C + abs(Maior_AB - C)) / 2

    #saída
    print(f"{Maior_ABC} eh o maior")

main()
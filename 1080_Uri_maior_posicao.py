def main():
    n = int(input("Digite um número: "))
    gambiarra = 0

    for i in range(1,100):
        n2 = int(input("Digite outro número: "))
        if n2 > gambiarra:
            maior = n2
            posicao = i+1
            gambiarra = n2
           
    print(maior)
    print(posicao)


if __name__ == "__main__":
    main()
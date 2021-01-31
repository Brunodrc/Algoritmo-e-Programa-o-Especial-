def main():
    testes = int(input("Quantos testes: "))

    for i in range(testes):
        n = int(input("Qual inteiro: "))
        soma = 0 

        for c in range(1, n):
            if n % c == 0:
                soma += c
        if soma == n:
            print(f"{n} eh perfeito.")
        else:
            print(f"{n} não eh perfeito.")

if __name__=="__main__":
    main()
def main():
    testes = int(input("Quantos testes: "))

    for i in range(testes):
        n = int(input("Qual inteiro: "))
        divisor = 0
        contador = 1

        while contador <= n:

            if n % contador == 0:
                divisor += 1
            
            contador += 1
       
        if divisor > 2:
            print(f"{n} não eh primo.")
        else:
            print(f"{n} eh primo.")

if __name__=="__main__":
    main()
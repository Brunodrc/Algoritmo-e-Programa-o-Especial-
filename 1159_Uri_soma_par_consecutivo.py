def main():
    while True:
        x = int(input("Qual inteiro: "))
        soma = 0
        contador = 1

        if x != 0:
            while contador <= 5:
                if x % 2 == 0: 
                    soma += x
                    x += 1
                    contador += 1
                else:
                    x += 1
            print(soma)
        
        if x == 0:
            break
if __name__=="__main__":
    main()
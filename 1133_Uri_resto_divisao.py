def main():
    valor1 = int(input("Digite um inteiro: "))
    valor2 = int(input("Digite um inteiro: "))
    

    if valor1 > valor2:
        for i in range(valor2, valor1):

            if i % 5 == 2 or i % 5 == 3:
                print(i)
         
    else:
        for i in range(valor1, valor2):
            if i % 5 == 2 or i % 5 == 3:
                print(i)

if __name__=="__main__":
    main()
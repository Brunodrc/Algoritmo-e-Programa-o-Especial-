def main():
    valor1 = int(input("Digite um inteiro: "))
    valor2 = int(input("Digite um inteiro: "))
    soma = 0

    if valor1 > valor2:
        for i in range(valor2, valor1 + 1):

            if i % 13 != 0:
                soma += i
         
    else:
        for i in range(valor1, valor2 + 1):
            if i % 13 !=0:
                soma += i
           
    print(soma)

if __name__=="__main__":
    main()
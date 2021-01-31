def main():
    idade = 0
    soma = 0
    qtd = 0

    while True:
        idade = int(input("digite uma idade: "))
        
        if idade >= 0:
            soma += idade
            qtd += 1
        else:
            break
    media = soma / qtd
    print(media)
if __name__=="__main__":
    main()
def main():
    qtd_testes = int(input("Digite o número de testes: "))


    for i in range(qtd_testes):
        entrada2 = input("Quais os dois inteiros: ") 
        dados = entrada2.split()
        valor1 = int(dados[0])
        valor2 = int(dados[1])
        soma = 0
        if valor1 > valor2:
            for n in range(valor2+1,valor1):
                if eh_impar(n):
                    soma += n
        elif valor1 < valor2:
            for x in range(valor1+1, valor2):
                if eh_impar(x):
                    soma += x
        else:
            soma = 0
        
        print(soma)

def eh_impar(numero_inteiro):
    if numero_inteiro % 2 != 0:
        return True

if __name__=="__main__":
    main()
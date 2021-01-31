def main():
    qtd_testes = int(input("Quantos testes: "))

    for i in range(qtd_testes):
        entrada = input("Digite dois números ")
        dados = entrada.split()
        x = int(dados[0])
        y = int(dados[1])
        if y == 0:
            print("divisão impossível")
        else:
            divisao = x / y
            print(f"{divisao:.1f}")

if __name__=="__main__":
    main()
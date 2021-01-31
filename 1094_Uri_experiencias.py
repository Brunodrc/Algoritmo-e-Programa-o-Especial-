def main():
    qtd_experimentos = int(input("Quantos testes: "))
    total_cobaia = 0
    total_coelho = 0
    total_rato = 0
    total_sapo = 0

    for i in range(qtd_experimentos):
        linha = input("Indique a quantidade e a cobaia: ")
        dados = linha.split()
        qtd_cobaia = int(dados[0])
        cobaia = dados[1]
        if cobaia == "C":
            total_coelho += qtd_cobaia
        elif cobaia == "R":
            total_rato += qtd_cobaia
        elif cobaia == "S":
            total_sapo += qtd_cobaia
        total_cobaia += qtd_cobaia
    
    porcentagem_coelho = calculo_porcentagem(total_cobaia, total_coelho)
    porcentagem_rato = calculo_porcentagem(total_cobaia, total_rato)
    porcentagem_sapo = calculo_porcentagem(total_cobaia, total_sapo)
    
    print(f"Total: {total_cobaia} cobaias")
    print(f"Total: {total_coelho} coelhos")
    print(f"Total: {total_rato} ratos")
    print(f"Total: {total_sapo} sapos")
    print(f"Percentual de coelhos:{porcentagem_coelho:.2f} %")
    print(f"Percentual de ratos:{porcentagem_rato:.2f} %")
    print(f"Percentual de sapos:{porcentagem_sapo:.2f} %")



def calculo_porcentagem(total, parte):
    porcentagem = (parte * 100) / total
    return porcentagem

if __name__ == "__main__":
    main()
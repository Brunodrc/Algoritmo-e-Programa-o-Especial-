def main():
    #ENTRADA
    linha1 = input().split()
    n1 = int(linha1[0])
    peca1 = int(linha1[1])
    valor1 = float(linha1[2])

    linha2 = input().split()
    n2 = int(linha2[0])
    peca2 = int(linha2[1])
    valor2 = float(linha2[2])

    #processamento
    total = (peca1 * valor1) + (peca2 * valor2)

    #SAIDA
    print(f"VALOR A PAGAR: R$ {total:.2f}")

main()
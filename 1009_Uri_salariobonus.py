def main():
    #ENTRADA
    #vend = input("Nome do vendedor: ")
    salario = float(input("Salário fixo: "))
    vendas = float(input("Qauntia vendida: ")) 

    #processamento
    total = salario + 0.15 * vendas

    #SAIDA
    print(f"TOTAL = R$ {total:.2f}")

main()
def main():
    salario = float(input("Digite o seu salário: "))

    if 0.00 <= salario <= 2000.00:
        print("Isento")

    elif 2000.00 < salario <= 3000.00:
        faixa = salario - 2000.00
        tributo = faixa * 0.08
        print(f"R$ {tributo:.2f}")
    
    elif 3000.00 < salario <= 4500.00:
        faixa1 = salario - 2000.00
        faixa3 = faixa1 - 1000.00
        faixa2 = faixa1 - faixa3
        tributo1 = faixa2 * 0.08
        tributo2 = faixa3 * 0.18
        tributo_total = tributo1 + tributo2
        print(f"R$ {tributo_total:.2f}")
    
    elif salario > 4500.00:
        faixa1 = salario - 2000.00
        faixa3 = salario - 4500.00
        faixa2 = faixa1 - 1000 - faixa3 
        total1 = faixa1 - faixa2 - faixa3
        tributo1 = total1 * 0.08
        tributo2 = faixa2 * 0.18
        tributo3 = faixa3 * 0.28
        tributo_total = tributo1 + tributo2 +tributo3
        print(f"R$ {tributo_total:.2f}")

if __name__ == "__main__":
    main()
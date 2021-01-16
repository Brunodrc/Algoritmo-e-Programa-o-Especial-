def main():
    salario_antes = float(input("Digite o salário: R$ "))

    if 0 < salario_antes <= 400.00:
        novo_salario = salario_antes + (salario_antes * 0.15)
        reajuste = novo_salario - salario_antes
        print(f"Novo salário: {novo_salario:.2f}")
        print(f"Reajuste: {reajuste:.2f}")
        print(f"Em percentual: 15 %")
    elif 400.01 <= salario_antes <= 800.00:
        novo_salario = salario_antes + (salario_antes * 0.12)
        reajuste = novo_salario - salario_antes
        print(f"Novo salário: {novo_salario:.2f}")
        print(f"Reajuste: {reajuste:.2f}")
        print(f"Em percentual: 12 %")
    elif 800.01 <= salario_antes <= 1200.00:
        novo_salario = salario_antes + (salario_antes * 0.10)
        reajuste = novo_salario - salario_antes
        print(f"Novo salário: {novo_salario:.2f}")
        print(f"Reajuste: {reajuste:.2f}")
        print(f"Em percentual: 10 %")
    elif 1200.01 <= salario_antes <= 2000.00:
        novo_salario = salario_antes + (salario_antes * 0.07)
        reajuste = novo_salario - salario_antes
        print(f"Novo salário: {novo_salario:.2f}")
        print(f"Reajuste: {reajuste:.2f}")
        print(f"Em percentual: 7 %")
    else:
        novo_salario = salario_antes + (salario_antes * 0.04)
        reajuste = novo_salario - salario_antes
        print(f"Novo salário: {novo_salario:.2f}")
        print(f"Reajuste: {reajuste:.2f}")
        print(f"Em percentual: 4 %")

if __name__ == "__main__":
    main()
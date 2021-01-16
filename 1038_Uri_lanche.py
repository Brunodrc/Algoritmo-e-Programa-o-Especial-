def main():
    entrada = input("Digite o código e a quantidade: ")
    linha = entrada.split()
    codigo = int(linha[0])
    quantidade = int(linha[1])

    if codigo < 0 or codigo > 5:
        print("código inexistente")
    elif codigo == 1:
        total = quantidade * 4.0
        print(f"TOTAL = R$ {total:.2f}")
    elif codigo == 2:
        total = quantidade * 4.5
        print(f"TOTAL = R$ {total:.2f}")
    elif codigo == 3:
        total = quantidade * 5.0
        print(f"TOTAL = R$ {total:.2f}")
    elif codigo == 4:
        total = quantidade * 2
        print(f"TOTAL = R$ {total:.2f}")
    else:
        total = quantidade * 1.5
        print(f"TOTAL = R$ {total:.2f}")

if __name__ == "__main__":
    main()
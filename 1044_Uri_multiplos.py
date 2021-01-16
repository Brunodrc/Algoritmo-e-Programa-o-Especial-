def main():
    entrada = input("Valores: ")

    dados = entrada.split()
    a = int(dados[0])
    b = int(dados[1])

    if a % b == 0 or b % a == 0:
        print("São Múltiplos")
    
    else:
        print("Não são Múltiplos")

if __name__ == "__main__":
    main()
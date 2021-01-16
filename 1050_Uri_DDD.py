def main():
    entrada = int(input("Digite o DDD: "))

    if entrada == 61:
        print("Brasília")
    elif entrada == 71:
        print("Salvador")
    elif entrada == 11:
        print("São Paulo")
    elif entrada == 21:
        print("Rio de Janeiro")
    elif entrada == 32:
        print("Juiz de Fora")
    elif entrada == 19:
        print("Campinas")
    elif entrada == 27:
        print("Vitória")
    elif entrada == 31:
        print("Belo Horizonte")
    else:
        print("DDD não cadastrado")

if __name__ == "__main__":
    main()
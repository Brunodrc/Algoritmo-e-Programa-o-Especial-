def main():
    senha = input("Digite a senha: ")

    while not senha == "2002":
        print("Senha Invalida")
        senha = input("Digite a senha: ")
    print("Acesso Permitido")

if __name__=="__main__":
    main()
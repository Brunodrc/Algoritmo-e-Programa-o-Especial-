def main():
    entrada = int(input("Digite o código: "))
    cont_alcool = 0
    cont_gasol = 0
    cont_diesel = 0

    while entrada != 4: 
        
        if entrada == 1:
            cont_alcool += 1
        elif entrada == 2:
            cont_gasol += 1
        elif entrada == 3:
            cont_diesel += 1

        entrada = int(input("Digite o código: "))
    
    print("MUITO OBRIGADO")
    print(f"Álcool: {cont_alcool}.")
    print(f"Gasolina: {cont_gasol}.")
    print(f"Diesel: {cont_diesel}.")

if __name__ == "__main__":
    main()
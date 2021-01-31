def main():
    
    soma = 0
    criterio_parada = 0
    
    while criterio_parada < 2:
        nota = float(input("Digite uma nota: "))

        if nota >= 0 and nota <= 10:
            soma += nota
            criterio_parada += 1

        else:
            print("nota inválida")
    
    media = soma / 2
    print(f"média = {media:.2f}")

if __name__=="__main__":
    main()
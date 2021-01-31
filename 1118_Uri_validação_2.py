def main():
    soma = 0
    criterio_parada = 0
    continuar = True

    while continuar == True:
        nota = float(input("Digite uma nota: "))
        
        if nota >= 0 and nota <= 10:
            soma += nota
            criterio_parada += 1
            
            

            if criterio_parada == 2:
                media = soma / 2
                print(f"média = {media:.2f}")
                criterio_parada = 0
                soma = 0

                while True:
                    novo_calculo = int(input("novo calculo (1-sim 2-nao): "))
                    if novo_calculo == 2:
                        continuar = False
                        break
                    elif novo_calculo == 1:
                        continuar = True
                        break
        else:
            print("nota inválida") 

if __name__=="__main__":
    main()
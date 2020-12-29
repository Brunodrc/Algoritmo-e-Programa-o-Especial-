def main():
    # entrada
    linha1 = input("Insira dois valores: ")
    linha2 = input("Insira dois valores: ")

    valores1 = linha1.split()
    x1 = float(valores1[0])
    y1 = float(valores1[1])

    valores2 = linha2.split()
    x2 = float(valores2[0])
    y2 = float(valores2[1])
    
    # processamento
    distancia = ((x2 - x1) **2 + (y2 - y1) **2) **0.5

    #saida
    print(f"{distancia:.4f}")

main()
def main():
    # entrada
    distancia = int(input("Distância em Km: "))
    gasto = float(input("Gasto em litros: "))

    # processamento
    consumo = distancia / gasto

    # saida
    print(f" {consumo:.3f} km/l")

main()
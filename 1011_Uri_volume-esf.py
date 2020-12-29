def main():
    # entrada
    raio = float(input("Digite o raio: "))

    #processamento
    volume = (4/3.0) * 3.14159 * (raio ** 3)

    #saida
    print(f"VOLUME = {volume:.3f}")

main()
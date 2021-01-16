def main():
    entrada = input("Valores: ")

    dados = entrada.split()
    a = float(dados[0])
    b = float(dados[1])
    c = float(dados[2])

    if a + b > c and a + c > b and b + c > a: 
        perimetro = a + b + c
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = ((a + b) * c) / 2
        print(f"Área = {area:.1f}")


if __name__ == "__main__":
    main()
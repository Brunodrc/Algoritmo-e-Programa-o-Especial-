def main():
    # entrada
    linha = input("Insira os dados: ")
    dados = linha.split()
    a = float(dados[0])
    b = float(dados[1])
    c = float(dados[2])

    # processamento
    triangulo = area_triangulo(a, c)
    circulo = area_circulo(c)
    trapezio = area_trapezio(a, b, c)
    quadrado = area_quadrado(b)
    retangulo = area_retangulo(a,b)

    # saida
    print(f"TRIANGULO = {triangulo:.3f}")
    print(f"CIRCULO = {circulo:.3f}")
    print(f"TRAPEZIO = {trapezio:.3f}")
    print(f"QUADRADO = {quadrado:.3f}")
    print(f"RETANGULO = {retangulo:.3f}")

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def area_circulo(raio):
    area = 3.14159 * (raio ** 2)
    return area

def area_trapezio(base1, base2, altura):
    area = ((base1 + base2) * altura) / 2
    return area

def area_quadrado(lado):
    area = lado * lado
    return area

def area_retangulo(base, altura):
    area = base * altura
    return area 

main()


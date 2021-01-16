def main():
    entrada = input("Digite 3 valores: ")

    dados = entrada.split()
    a = float(dados[0])
    b = float(dados[1])
    c = float(dados[2])

    if (a>b>c)or(a==b>c)or(a==b>c) or(a==b==c):
        ladoA = a
        ladoB = b
        ladoC = c
    elif (a>c>b)or(a==c>b)or(a>c==b):
        ladoA = a
        ladoB = c
        ladoC = b
    elif (b>a>c)or(b==a>c)or(b>a==c):
        ladoA = b
        ladoB = a
        ladoC = c
    elif (b>c>a)or(b==c>a)or(b>c==a):
        ladoA = b
        ladoB = c
        ladoC = a
    elif (c>a>b)or(c==a>b)or(c>a==b):
        ladoA = c
        ladoB = a
        ladoC = b
    elif (c>b>a)or(c==b>a)or(c>b==a):
        ladoA = c
        ladoB = b
        ladoC = a 
    
    if ladoA >= ladoB + ladoC:
        print(" NAO FORMA TRIANGULO")
    else:
        if ladoA ** 2 == (ladoB**2) + (ladoC**2):
            print("TRIANGULO RETANGULO")
        elif ladoA ** 2 > (ladoB **2) + (ladoC **2):
            print("TRIANGULO OBTUSANGULO")
        elif ladoA ** 2 < (ladoB **2) + (ladoC **2):
            print("TRIANGULO ACUTANGULO")
    if ladoA == ladoB == ladoC:
        print("TRIANGULO EQUILATERO")
    elif ladoA == ladoB != ladoC or ladoB == ladoC != ladoA or ladoA == ladoC != ladoB:
        print("TRIANGULO ISOSCELES")

if __name__ == "__main__":
    main()
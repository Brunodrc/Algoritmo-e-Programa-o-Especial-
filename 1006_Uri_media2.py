def main():
    #ENTRADA
    nota1 = float(input("Qual a primeira nota: "))
    nota2 = float(input("Qual a segunda nota: "))
    nota3 = float(input("Qual a terceira nota: "))

    #processamento

    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10

    #SAIDA

    print(f"MEDIA = {media:.1f}")

main()
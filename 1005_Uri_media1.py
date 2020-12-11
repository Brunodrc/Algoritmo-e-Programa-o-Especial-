def main():
    #ENTRADA
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    #processamento

    media = ((nota1 * 3.5) + (nota2 * 7.5))/ 11

    #SAIDA

    print(f"MEDIA = {media:.5f}") 

main()
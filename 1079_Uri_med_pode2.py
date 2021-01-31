"""def main():
    n = int(input("Quantidade de testes: "))
    contador = 0

    while contador <= n:
        dados = input("Digite os valores: ")
        formatar = dados.split()
        dado1 = float(formatar[0]) 
        dado2 = float(formatar[1]) 
        dado3 = float(formatar[2])
        media_pod = ((dado1 * 2) + (dado2 * 3) + (dado3 * 5)) / (2 + 3 + 5)
        print("{:.1f}",format(media_pod))
        contador += 1  

if __name__== "__main__":
    main()"""

#Resposta um pouco aprimorada
def main():
    n = int(input("Quantidade de testes: "))

    for i in range(n):
        dados = input("Digite os valores: ")
        formatar = dados.split()
        dado1 = float(formatar[0]) 
        dado2 = float(formatar[1]) 
        dado3 = float(formatar[2])
        media_pod = media_ponderada(dado1, dado2, dado3)
        print(f"{media_pod:.1f}")

def media_ponderada(valor1, valor2, valor3):
    media = ((valor1 * 2) + (valor2 * 3) + (valor3 * 5)) / (2 + 3 + 5)
    return media

if __name__== "__main__":
    main()

def main():
    soma = 1
    denominador = 2
    contador = 3

    while contador < 40:
        soma += float(contador) / float(denominador)
        denominador *= 2
        contador += 2
    
    print(f"{soma:.2f}")

if __name__=="__main__":
    main()
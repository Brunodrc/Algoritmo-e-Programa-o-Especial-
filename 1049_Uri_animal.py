def main():
    caracter1 = input("Digite a palavra chave: ")
    caracter2 = input("Digite a característica 2: ")
    caracter3 = input("Digite a característica 3: ")

    if caracter1 == "vertebrado" and caracter2 == "mamifero" and caracter3 == "onivoro":
        print("homem")
    elif caracter1 == "vertebrado" and caracter2 == "mamifero" and caracter3 == "herbivoro":
        print("vaca")
    elif caracter1 == "vertebrado" and caracter2 == "ave" and caracter3 == "onivoro":
        print("pomba")
    elif caracter1 == "vertebrado" and caracter2 == "ave" and caracter3 == "carnivoro":
        print("aguia")
    elif caracter1 == "invertebrado" and caracter2 == "inseto" and caracter3 == "hematofago":
        print("pulga")
    elif caracter1 == "invertebrado" and caracter2 == "inseto" and caracter3 == "herbivoro":
        print("lagarta")
    elif caracter1 == "invertebrado" and caracter2 == "anelideo" and caracter3 == "hematofago":
        print("sanguessuga")
    elif caracter1 == "invertebrado" and caracter2 == "anelideo" and caracter3 == "onivoro":
        print("minhoca")

if __name__ == "__main__":
    main()
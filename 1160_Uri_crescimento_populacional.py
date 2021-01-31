def main():
    testes = int(input("Quantos testes: "))

    for i in range(testes):
        entrada = input("Digite os valores: ")
        dados = entrada.split()
        pa = int(dados[0])
        pb = int(dados[1])
        cres_a = float(dados[2])
        cres_b = float(dados[3])

        anos = 0

        while pa <= pb:
            cres_pa = pa * (cres_a/100)
            cres_pb = pb * (cres_b/100)
            anos += 1
            pa += cres_pa
            pb += cres_pb

            if anos > 100:
                break
        if anos > 100: 
            print("Mais de 1 século.")
        else:
            print(f"{anos} anos.")


if __name__=="__main__":
    main()
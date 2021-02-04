def main():
    vetor = []

    for i in range(100):
        a = float(input("Valor: "))
        vetor.append(a)
        if a <= 10:
            print(f"A[{i}] = {vetor[i]} ")
        

if __name__=="__main__":
    main()
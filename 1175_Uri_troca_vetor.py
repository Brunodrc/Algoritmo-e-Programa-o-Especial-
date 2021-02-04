def main():
    vetor = []

    for i in range(20):
        a = int(input("Valor: "))
        vetor.append(a)
    
    for invertido in range(vetor[20], vetor[0],-1):
        print(f"N[{invertido}]= {vetor[invertido]}")
        
if __name__=="__main__":
    main()
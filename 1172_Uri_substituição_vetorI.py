def main():
    vetor = [1,2,3,4,5,6,7,8,9,10]

    for i in range(len(vetor)):
        
        vetor[i] = int(input(f"Numero {i}: "))
        
        if vetor[i] <= 0:
            vetor[i] = 1
        
        print(f"Vetor [{i}] = {vetor[i]} ")
        

if __name__=="__main__":
    main()
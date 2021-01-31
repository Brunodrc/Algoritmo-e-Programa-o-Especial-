def main():
    n = int(input("Qual inteiro: "))
    sequencia = 1

    for i in range(1, n+1):
    
        print(f"{sequencia} {sequencia + 1} {sequencia + 2} PUM")
        sequencia += 4

if __name__=="__main__":
    main()
def main():
    while True:
        n = int(input("Qual inteiro: "))

        if n == 0:
            break

        for i in range(1, n+1):
                print(f"{i}", end=" ")
        print(" ")
    
if __name__=="__main__":
    main()
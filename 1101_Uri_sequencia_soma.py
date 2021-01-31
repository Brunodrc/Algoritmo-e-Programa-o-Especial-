def main():
    entrada = input("Indique os dois valores: ")
    dados = entrada.split()
    m = int(dados[0])
    n = int(dados[1])
    soma = 0

    if m == 0 or n == 0:
        soma = 0
    
    elif m < n:
        for m in range(m, n+1):
            print(m, end=" ")
            soma += m
        print(f"sum= {soma}")
    
    elif  m > n:
        for n in range(n,m+1):
            print(n, end=" ")
            soma += n
        print(f"sum= {soma}")

if __name__=="__main__":
    main()
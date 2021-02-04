def main():
    
    testes =int(input("Quantos testes: "))
    
    for i in range(testes):
        
        x=int(input("Digite um valor: "))
        f=[0,1]
        
        if x>1:
            for c in range(2,x+1):
           
                f.append(f[c-2] +f [c-1])

            print('Fib({}) = {}'.format(x,f[x]))
        
        if x <=1:
            print('Fib({}) = {}'.format(x,f[x]))

if __name__=="__main__":
    main()
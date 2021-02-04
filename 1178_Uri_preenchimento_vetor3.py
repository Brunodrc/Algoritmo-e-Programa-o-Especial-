def main():
    x = float(input("qual valor: "))
    n = []
    x *= 2
    for i in range(100):
        n.append(x)
        print(f"N[{i}] = {(x/2):.4f}")
        x=x/2

if __name__=="__main__":
    main()
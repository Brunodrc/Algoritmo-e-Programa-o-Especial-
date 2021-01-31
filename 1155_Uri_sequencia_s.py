def main():
    soma = 0

    for i in range(1,101):
        soma += 1/float(i)

    print(f"{soma:.2f}")

if __name__=="__main__":
    main()
def main():
    i = 0
    j = 1
    acrescimo = 0
    contador1 = 0
    contador2 = 0

    while i <= 2:
        if contador2 == 0:
            print(f"I = {i:.0f} J= {j:.0f}")
        else:
            print(f"I = {i:.1f} J = {j:.1f}")
        contador1 += 1

        if contador1 == 3:
            i += 0.2
            acrescimo += 0.2
            j = acrescimo
            contador1 = 0
            contador2 += 1
        if contador2 == 5:
            contador2 = 0
        j += 1
if __name__=="__main__":
    main()
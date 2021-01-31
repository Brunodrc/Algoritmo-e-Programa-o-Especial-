def main():
    vitoria_gremio = 0
    vitoria_inter = 0
    empates = 0

    while  True:
        entrada = (input("Número de gols de Inter e Grêmio: "))

        valores = entrada.split()
        gols_inter = int(valores[0])
        gols_gremio = int(valores[1])
        
        if gols_gremio == gols_inter:
            empates += 1
        
        else:
            if gols_inter > gols_gremio:
                vitoria_inter += 1
            else:
                vitoria_gremio += 1
        
        novo_grenal = int(input("Novo grenal (1-sim 2-nao): "))
        if novo_grenal == 2:
            break

    total_grenais = vitoria_inter + vitoria_gremio + empates
    
    print(f"{total_grenais} grenais")
    print(f"Inter: {vitoria_inter}")
    print(f"Grêmio: {vitoria_gremio}")
    print(f"Empates: {empates}")

    if vitoria_inter == vitoria_gremio:
        print("Não houve vencedor")
    else:
        if vitoria_inter > vitoria_gremio:
            print("Inter venceu mais.")
        else:
            print("Grêmio venceu mais.")

if __name__=="__main__":
    main()
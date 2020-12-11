def main():
    #ENTRADA
    funcionario = int(input("Digite o número do func.: "))
    horas = int(input("Digite as horas trabalhadas: "))
    valor_h = float(input("Digite o valor recebido por hora: "))

    #processamento
    
    salario = horas * valor_h

    #SAIDA
    print(f"NUMBER = {funcionario}")
    print(f"SALARIO = R$ {salario:.2f}") 

main()
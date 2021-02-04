import os
import json

def main():
    
    #inicilizar (recuperar banco de dados)

    celulares = inicializar("arquivo_celulares.csv")

    menu = tela_principal()
    opção = int(input(menu)) #elaborar uma função recursiva q peça o input adequado

    while opção != 0:
        if opção == 1:
            celular = novo_celular()

            #salvando o objeto
            celulares.append(celular)
            print("Celular salvo com sucesso!")

        elif opção == 2:
            
        
        input("<enter> para continuar...")
        opção = int(input(menu))

    #finalizar(salvar informações digitadas no arquivo de dados)
        finalizar("arquiarquivo_celulares.csv", celulares)

def tela_principal():
    menu = ">>>>> Aplicativo de celulares <<<<<\n"
    menu += "1 - Novo celular\n"
    menu += "2 - Listar celulares cadastrados\n"
    menu += "0 - Sair\n"
    menu += "\nopção:::> "

    return menu

#percistência de dados
def inicilizar(nome_arquivo):
    celulares_arquivo = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, "r")
        dados = arquivo.readline()
        arquivo.close() 
        celulares_arquivo = json.loads(dados)
   
    return celulares_arquivo

def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)
    salvar = open(nome_arquivo, "w")
    salvar.write(dados)
    salvar.close

def novo_celular():
    print("Criando novo celular")
    #obtendo os dados
    nome = input("Nome: ")
    marca = input("Marca: ")
    tela = input("Tela(pol.): ")
    valor = float(input("Valor (R$): "))
    camera_front = input("Camera frontal (simn/não): ")

    #criando o objeto
    celular = {}
    celular["nome"] = nome
    celular["marca"] = marca
    celular["tela"] = tela
    celular["valor"] = valor
    celular["camera_front"] = camera_front

    return celular

def mostrar_celular(celulares):
    qtd = len(celulares)
    print(f"Há {qtd} celulare(s) cadastrado(s)")

    for celular in celulares:
        print("Nome:", celular["nome"])
        print("Marca:", celular["marca"])
        print("Valor:", celular["valor"])
        print(12 *"__")

if __name__=="__main__":
    main()
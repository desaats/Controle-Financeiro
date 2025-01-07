import os 

def nome_do_programa():

    texto = ("""𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐅𝐈𝐍𝐀𝐍𝐂𝐄""")

    linha = "*" * (len(texto)+ 5)
    print(linha)
    print(texto)
    print(linha)

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")
    
    opcao = int(input("Digite uma opção valida: "))
    return escolha_opcao(opcao)
    
def escolha_opcao(opcao):
    
     match opcao:
        case 1:
            print("Você escolheu o credito")
            #novo_credito()
        case 2:
            print("Você escolheu o debito")
            novo_debito()
        case 3:
            print("Você escolheu o extrato")
            #mostrar_extrato()
        case 4:
            print("Finalizando o aplicativo")
            #finalizar_app()
        case _:
            print("Digite alguma opção valida: ")
            
     return exibir_opcoes()


def novo_debito():
    receita = 2450
    gasto = float(input("Digite o valor gasto: "))
    valor_atualizado = receita - gasto
    print(f"Valor atualizado: {valor_atualizado}")


def main():
    os.system("cls")
    nome_do_programa()
    exibir_opcoes()
    
    

if __name__ == "__main__":
    main()


import os 

def nome_do_programa():

    texto = ("""𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐅𝐈𝐍𝐀𝐍𝐂𝐄""")

    linha = "*" * (len(texto)+ 5)
    print(linha)
    print(texto)
    print(linha)

def exibir_opcoes():
    print("1. Creditar na conta")
    print("2. Debitar na conta")
    print("3. Mostrar extrato do ultimo mês")
    print("4. Sair\n")
    
    opcao = int(input("Digite uma opção valida: "))
    return escolha_opcao(opcao)

def saldo_conta():
    saldo = 3000
    return saldo

def novo_debito():
    receita = saldo_conta()
    debito = float(input("Digite o valor a debitar: "))
    valor_a_debitar = receita - debito
    print(f"Valor atualizado: {valor_a_debitar}")

def novo_credito():
    receita = saldo_conta()
    credito = float(input("Digite o valor a creditar "))
    valor_a_creditar = receita + credito
    print(f"Valor atualizado: {valor_a_creditar}")
    
def escolha_opcao(opcao):
    
     match opcao:
        case 1:
            novo_credito()
        case 2:
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



def main():
    os.system("cls")
    nome_do_programa()
    exibir_opcoes()
    
    

if __name__ == "__main__":
    main()


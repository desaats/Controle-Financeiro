import os 
import time
from modelos.contas.conta import Conta

def nome_do_programa():

    texto = ("""𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐅𝐈𝐍𝐀𝐍𝐂𝐄""")

    linha = "*" * (len(texto)+ 5)
    print(linha)
    print(texto)
    print(linha)

def exibir_opcoes():
    print("1. Creditar na conta")
    print("2. Debitar na conta")
    print("3. Mostra lista de contas Cadastradas")
    print("4. Mostrar extrato do ultimo mês")
    print("5. Sair\n")
    opcao = int(input("Digite uma opção valida: "))
    return opcao

def limpando_terminal():
    time.sleep(3)
    os.system("cls")

def solicitar_id_valido():
    while True:
        try:
            id_procurado = int(input("Digite o ID da conta: "))
            conta = Conta.buscar_id(id_procurado)
            if conta:
               return conta 
            else:
               print("ID inválido. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número inteiro válido")

def novo_credito():
    conta = solicitar_id_valido()
    credito = float(input("Digite o valor a creditar: "))
    if credito > 0:
       conta._saldo += credito
       return print(f"Novo saldo: {conta._saldo:.2f}")
    else:
        return print(f"Valor inválido")
    
def novo_debito():
    conta = solicitar_id_valido()
    debito = float(input("Digite o valor a debitar: "))
    if 0 < debito:
       conta._saldo -= debito
       return print(f"Novo saldo: {conta._saldo:.2f}")
    else:
        return print(f"Valor inválido")
     
def main():
    os.system("cls")
    nome_do_programa()
    
    Conta("Alan Torres", "000001", "Banco Inter")._saldo = 3000
    Conta("Alan Torres", "154132", "Banco Nubank")._saldo = 2000
    Conta("Alan Torres", "151501", "Corretora Rico")._saldo = 1000
    Conta("Alan Torres", "065241", "Banco Caixa")._saldo = 0
    
    while True:
        opcao = exibir_opcoes()
        if opcao == 1:
            novo_credito()
            limpando_terminal()
        elif opcao == 2:
            novo_debito()
            limpando_terminal()
        elif opcao == 3:
            Conta.listar_contas()
            limpando_terminal()
        elif opcao == 4:
            mostrar_extratos()
        elif opcao == 5:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente Novamente.")
            limpando_terminal()
    

if __name__ == "__main__":
    main()


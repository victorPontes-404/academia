from funcoes.utilitarios import limpar, delay
from funcoes.user import cadastrar, login, cadastrar_secundario
from sistema_interno.interno import opcoes_usuario, interface_base
from pwinput import pwinput

while True:
    limpar()

    try:
        print("\n1-adicionar usuario\n2-entrar\n3-sair do programa")

        opc = int(input("\ndigite a opção: "))

        match (opc):
            #opçoes de entrada\saida do sistema
            case 1:
                email = input("\ndigite o seu email: ")
                senha =  pwinput("digite a sua senha: ")
                id_aluno = cadastrar(email, senha)
                
                if id_aluno:
                    limpar()
                    print("mais alguns dados para finalizar o cadastro\n")

                    nome = input("digire o seu nome: ")
                    idade = int(input("digite a sua idade: "))
                    cadastrar_secundario(id_aluno, nome, idade)

            case 2:
                email = input("\ndigite o seu email: ")
                senha = pwinput("digite a sua senha: ")
                
                logado = login(email, senha)

                if logado:
                    delay(5)
                    interface_base(logado)

            case 3:
                break


    except ValueError:
        print("digite um numero")

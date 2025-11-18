from funcoes.user import deletar_user


def opcoes_usuario():
    try:
        while True:
            print("1-deletar usuario\n2-mudar senha\n3-mudar nome\n4-voltar")
            opc = input("digitea opção:")
            match opc:
                case 1:
                    deletar_user()
                case 2:
                    mudar_senha()
                case 4:
                    break
    except Exception as e:
        print(e)


def sistema():
    print("bem vindo!")

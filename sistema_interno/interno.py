from funcoes.user import deletar_user, visualizar_treinos, modificar_treino
from funcoes.utilitarios import limpar, delay

def interface_base(usuario):
    try:
        while True:
            limpar()
            print("1-visualizar os seus treinos\n2-visualizar os horarios das modalidades\n3-modificar o seu treino\n4-opçoes do usuario\n5- sair")

            opc = int(input("digite a opção: "))
            match opc:
                case 1:
                    visualizar_treinos(usuario[0])
                case 3:
                    modificar_treino()
                case 5:
                    break
    except ValueError:
        print("digite um valor valido")
        delay(5)


def opcoes_usuario():
    try:
        while True:
            print("1-deletar usuario\n2-mudar senha\n3-mudar nome\n4-voltar")
            opc = input("digite a opção: ")
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

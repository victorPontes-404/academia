from config.db import conexao
from funcoes.utilitarios import delay

def cadastrar(email: str, senha: str):
    try:
        con = conexao()
        cursor = con.cursor()

        sql = "insert into alunos (email, senha) values (%s, %s)"
        cursor.execute(sql, (email, senha))
        con.commit()
        print("usuario cadastrado")
        

    except Exception as e:
        print(f"erro {e}")

    finally:
        cursor.close()
        con.close()
        delay(10)


def login(email: str, senha: str):
    con = conexao()
    cursor = con.cursor()

    sql ="select * from alunos where email=%s AND senha=%s"

    cursor.execute(sql, (email, senha))
    user = cursor.fetchone()

    if not user:
        return None
    
    deletado = user[6]

    if deletado:
        print("usuario deletado")
        return None


    return user


def cadastrar_secundario(nome: str, idade: int):
    try:
        con = conexao()
        cursor = con.cursor()

        sql = "incert into alunos (nome, idade) values (%s, %s)"
        cursor.execute(sql, (nome, idade))
        con.commit()
        print("dados do usuario completos")

    except Exception as e:
        print(f"erro {e}")

    finally:
        cursor.close()
        con.close()
        delay(5)



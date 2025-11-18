from config.db import conexao
from funcoes.utilitarios import delay

def cadastrar(email: str, senha: str):
    try:
        con = conexao()
        cursor = con.cursor()

        sql = "insert into alunos (email, senha) values (%s, %s)RETURNING id_aluno"
        cursor.execute(sql, (email, senha))
        
        print("usuario cadastrado")
        id_novo_aluno = cursor.fetchone()[0]
        con.commit()
        return id_novo_aluno

    except Exception as e:
        print(f"erro {e}")

    finally:
        cursor.close()
        con.close()
        delay(5)


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


def cadastrar_secundario(id_aluno: str, nome: str, idade: int):
    try:
        con = conexao()
        cursor = con.cursor()

        sql = "UPDATE alunos SET nome = %s, idade = %s WHERE id_aluno = %s"
        cursor.execute(sql, (nome, idade, id_aluno))
        con.commit()
        print("dados do usuario completos")

    except Exception as e:
        print(f"erro {e}")

    finally:
        cursor.close()
        con.close()
        delay(5)


def deletar_user(id_aluno):
    try:
        con = conexao()
        cursor = con.cursor()

        sql = "UPDATE Alunos SET deletado = TRUE WHERE id_aluno = %s"
        cursor.execute(sql, (id_aluno))
        con.commit
        print("usuario deletado com sucesso!")
    finally:
        cursor.close()
        con.close()
        delay(5)
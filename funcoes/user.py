from config.db import conexao
from funcoes.utilitarios import delay

def cadastrar(email: str, senha: str):
    try:
        con = conexao()
        cursor = con.cursor()

        #insere o email e senha em usuarios
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

    # Seleciona apenas o necessário
    sql = """
        SELECT id_aluno, nome, idade, condicionamento, email, senha, deletado, admin
        FROM alunos
        WHERE email = %s AND senha = %s
    """

    cursor.execute(sql, (email, senha))
    user = cursor.fetchone()

    # Nenhum usuário encontrado
    if not user:
        print("Email ou senha incorretos.")
        return None
    
    # user[6] => deletado
    deletado = user[6]

    if deletado:
        print("Esse usuário foi deletado.")
        return None
    
    # user[7] => admin
    eh_admin = user[7]

    # Retorna um dicionário, bem mais fácil de usar
    return {
        "id": user[0],
        "nome": user[1],
        "admin": eh_admin
    }


def cadastrar_secundario(id_aluno: str, nome: str, idade: int):
    try:
        con = conexao()
        cursor = con.cursor()

        #adiciona nome e idade em alunos
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

        #soft delete no user
        sql = "UPDATE Alunos SET deletado = TRUE WHERE id_aluno = %s"
        cursor.execute(sql, (id_aluno))
        con.commit()
        print("usuario deletado com sucesso!")
    finally:
        cursor.close()
        con.close()
        delay(5)


def deletar_treino(id_treino: int):
    try:
        con = conexao()
        cursor = con.cursor()

        sql = "DELETE FROM treinos WHERE id_treino = %s;"
        cursor.execute(sql, (id_treino,))
        con.commit()

        print(f"Treino com ID {id_treino} deletado com sucesso.")

    except Exception as e:
        print(f"Erro ao deletar treino: {e}")

    finally:
        cursor.close()
        con.close()


def visualizar_treinos(id_usuario: int):
    try:
        con = conexao()
        cursor = con.cursor()

        sql = """
            SELECT 
                a.nome AS aluno,
                p.tipo AS plano,
                p.valor,
                t.tipo_treino
            FROM alunos a
            INNER JOIN planos p ON a.id_aluno = p.id_aluno
            INNER JOIN treinos t ON a.id_aluno = t.id_aluno
            WHERE a.id_aluno = %s;
        """

        cursor.execute(sql, (id_usuario,))
        resultados = cursor.fetchall()

        if not resultados:
            print("Nenhum treino encontrado para este aluno.")
            return

        for linha in resultados:
            aluno = linha[0]
            plano = linha[1]
            valor = linha[2]
            treino = linha[3]

            print(f"Aluno: {aluno} | Plano: {plano} | Valor: R$ {valor} | Treino: {treino}")

    except Exception as e:
        print(f"Erro ao buscar dados: {e}")

    finally:
        cursor.close()
        con.close()

def listar_alunos_modalidades_treinos():
    try:
        con = conexao()
        cursor = con.cursor()

        sql = """
            SELECT
                a.nome AS aluno,
                m.tipo AS modalidade,
                m.horario,
                t.tipo_treino
            FROM alunos a
            INNER JOIN modalidades m ON a.id_aluno = m.id_aluno
            INNER JOIN treinos t ON m.id_treino = t.id_treino;
        """

        cursor.execute(sql)
        resultados = cursor.fetchall()

        # Mostrar os resultados
        for linha in resultados:
            aluno = linha[0]
            modalidade = linha[1]
            horario = linha[2]
            treino = linha[3]

            print(f"Aluno: {aluno} | Modalidade: {modalidade} | Horário: {horario} | Treino: {treino}")

    except Exception as e:
        print(f"Erro ao buscar modalidades: {e}")

    finally:
        cursor.close()
        con.close()


def modificar_treino(id_aluno, tipo, tipo_treino):
    try:
        con = conexao()
        cursor = con.cursor()

        sql = "INSERT INTO treinos (id_aluno, tipo, tipo_treino) VALUES (%s, %s, %s)"

        cursor.execute(sql, (id_aluno, tipo, tipo_treino))
        con.commit()

        print(f"Treino '{tipo_treino}' adicionado para o aluno {id_aluno} com sucesso.")

    except Exception as e:
        print(f"Erro ao adicionar treino: {e}")

    finally:
        cursor.close()
        con.close()

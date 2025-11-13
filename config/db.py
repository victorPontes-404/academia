import psycopg2


DB_HOST = "localhost"
DB_PORT = "5432"      
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "postgres"


def conexao():
    """
    criar conexão com o banco de dados
    """
    try:
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        print("conexao com sucesso")
        return conn
    except Exception as e:
        print(f"erro de conexão {e}")
        return None

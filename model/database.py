import mysql.connector as mc
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv


class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_NAME')
        self.password = getenv('DB_PSWD')
        self.database = getenv('DB_NAME')
        self.connection = None
        self.cursor = None

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""

        try:
            self.connection = mc.connect(
                host=self.host,
                database=self.database,
                user=self.username,
                password=self.password  # Corrigido: pswd para password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("Conexão com o Banco de Dados Realizada Com Sucesso!")
        except Error as e:
            print(f'Erro de Conexão: {e}')
        finally:  # Usando finally para garantir o fechamento em caso de erro
            if self.connection and not self.connection.is_connected():
                self.desconectar()

    def desconectar(self):
        """Encerra a conexão com o banco de dados e o cursor, se existirem."""

        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

        print('Conexão com o banco de dados encerrada com sucesso!')

    def consultar(self, sql, params=None):
        """Executa uma instrução SQL no banco de dados."""
        if not self.connection or not self.cursor:  # Verificação mais robusta
            print('Conexão ao banco de dados não estabelecida!')
            return None

        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except Error as e:
            print(f'Erro de execução: {e}')
            return None
        
    def executar(self, sql, params=None):
        """Executa uma instrução no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida!')
            return None

        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f'Erro de execução: {e}')
            return None


# Área 51
db = Database()
db.conectar()
db.consultar('SELECT * FROM tarefa')  # Corrigido: select para SELECT
db.desconectar() # desconectando do banco de dados
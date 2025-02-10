import mysql.connector # Biblioteca do connector do MySql
from mysql.connector import Error # Importando a classe Error para tratar as mensagens de erro do codigo
from dotenv import load_dotenv # Importando a função load_dotenv
from os import getenv # Importando a função getenv


class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_NAME')
        self.password = getenv('DB_PSWD')
        self.database = getenv('DB_NAME')
        self.connection = None # inicialização da conezão
        self.cursor = None # inicialização do cursor

def conectar(self):
    """Estabelece uma conexão com o banco de adados."""

    try:
        self.connection = mysql.connector.connect(
            host = self.host,
            database = self.database,
        b)
from database import Database

class Tarefa:
    def __init__(self, id, titulo, data_conclusao):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao

    def SalvarTarefa(self):
        """Salva Uma Nova Tarefa no Banco de Dados."""
        db = Database()
        db.conectar()

        sql = 'INSERT INTO tarefa (titulo, data_conclusao) VALUES (%s, %s)'
        params = (self.titulo, self.data_conclusao)
        db.executar(sql, params)
        db.desconectar()

    def listarTarefas():
        """Retornar uma lista com todas as tarefas cadastradas."""
        db = Database()
        db.conectar()

        sql = ('SELECT id, titulo, data_conclusao FROM tarefa')
        tarefas = db.consultar(sql)
        db.desconectar()
        return tarefas if tarefas else[]
    
    def apagarTarefa(self):
        """Apaga uma Tarefa cadastrada no banco de dados."""
        db = Database()
        db.conectar()

        sql = 'DELETE FROM tarefa WHERE id = %s'
        params = (self.id,)
        db.executar(sql, params)
        db.desconectar()
    
# Area 51
tarefa = Tarefa(1,'Teste de Tarefa', None)
from database import BancoDeDados
from model import Tarefa

class TarefaDAO:
    def __init__(self):
        # Pega a instância única do banco
        self.db = BancoDeDados()

    def salvar(self, tarefa: Tarefa):
        sql = "INSERT INTO tarefas (descricao) VALUES (?)"
        self.db.cursor.execute(sql, (tarefa.descricao,))
        self.db.conexao.commit()

    def listar_todos(self) -> list[Tarefa]:
        sql = "SELECT id, descricao FROM tarefas"
        self.db.cursor.execute(sql)
        
        lista_tarefas = []
        for linha in self.db.cursor.fetchall():
            # Converte a tupla do banco (id, desc) para Objeto Tarefa
            t = Tarefa(id=linha[0], descricao=linha[1])
            lista_tarefas.append(t)
        
        return lista_tarefas

    def remover(self, id_tarefa: int) -> bool:
        sql = "DELETE FROM tarefas WHERE id = ?"
        self.db.cursor.execute(sql, (id_tarefa,))
        self.db.conexao.commit()
        return self.db.cursor.rowcount > 0
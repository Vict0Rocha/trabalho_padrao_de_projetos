from dao import TarefaDAO
from factory import TarefaFactory
from database import BancoDeDados

class SistemaTarefasFacade:
    def __init__(self):
        self.dao = TarefaDAO()

    def registrar_tarefa(self, descricao: str):
        # 1. Pede para a Fábrica criar o objeto
        nova_tarefa = TarefaFactory.criar(descricao)
        # 2. Pede para o DAO salvar o objeto
        self.dao.salvar(nova_tarefa)
        print("Tarefa registrada com sucesso!")

    def obter_todas_tarefas(self):
        return self.dao.listar_todos()

    def excluir_tarefa(self, id_tarefa: int):
        sucesso = self.dao.remover(id_tarefa)
        if sucesso:
            print("Tarefa removida.")
        else:
            print("Erro: ID não encontrado.")

    def encerrar_sistema(self):
        # Fecha a conexão do Singleton
        BancoDeDados().fechar()
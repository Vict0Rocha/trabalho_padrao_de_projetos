from model import Tarefa

class TarefaFactory:
    @staticmethod
    def criar(descricao: str) -> Tarefa:
        if not descricao:
            raise ValueError("A descrição da tarefa não pode ser vazia.")
        
        # Aqui a fábrica "fabrica" o objeto
        return Tarefa(descricao=descricao)
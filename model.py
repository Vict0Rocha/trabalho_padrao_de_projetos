class Tarefa:
    def __init__(self, descricao: str, id: int = None): #type: ignore
        self.id = id
        self.descricao = descricao

    def __repr__(self):
        return f"Tarefa(id={self.id}, descricao='{self.descricao}')"
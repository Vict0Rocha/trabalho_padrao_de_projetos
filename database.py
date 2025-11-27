# Arquivo: database.py
import sqlite3
from typing import Optional

class BancoDeDados:
    _instancia: Optional['BancoDeDados'] = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(BancoDeDados, cls).__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        
        # Cria conexão e cursor
        self.conexao = sqlite3.connect("todo_list.db")
        self.cursor = self.conexao.cursor()
        self._criar_tabela()
        self._inicializado = True
        print("[Log] - Banco conectado (Singleton).")

    def _criar_tabela(self):
        sql = """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
        )
        """
        self.cursor.execute(sql)
        self.conexao.commit()

    def fechar(self):
        if self.conexao:
            self.conexao.close()
            BancoDeDados._instancia = None
            print("[Log] - Conexão fechada.")
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                               QLineEdit, QPushButton, QListWidget, 
                               QListWidgetItem, QMessageBox, QLabel, QFrame)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from facade import SistemaTarefasFacade

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        # 1. Inicializa a Fachada
        self.sistema = SistemaTarefasFacade()

        # 2. Configurações da Janela
        self.setWindowTitle("Task Master Pro")
        self.setGeometry(100, 100, 450, 600)
        
        # --- ESTILIZAÇÃO (CSS/QSS) ---
        # Aqui definimos as cores, bordas e fontes de toda a aplicação
        self.setStyleSheet("""
            QWidget {
                background-color: #2b2d42; /* Fundo Azul Escuro */
                color: #edf2f4;           /* Texto Claro */
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            
            QLabel#Titulo {
                font-size: 24px;
                font-weight: bold;
                color: #8d99ae;
                margin-bottom: 10px;
            }

            QLineEdit {
                background-color: #8d99ae;
                color: #2b2d42;
                border: 2px solid #2b2d42;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 2px solid #ef233c; /* Borda vermelha ao clicar */
                background-color: #edf2f4;
            }

            QPushButton {
                background-color: #ef233c; /* Vermelho Moderno */
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #d90429; /* Escurece ao passar o mouse */
            }
            QPushButton:pressed {
                background-color: #a80020;
            }

            QListWidget {
                background-color: #edf2f4;
                color: #2b2d42;
                border-radius: 8px;
                padding: 5px;
                border: none;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #dcdcdc;
            }
            QListWidget::item:selected {
                background-color: #8d99ae;
                color: white;
                border-radius: 5px;
            }
        """)

        # 3. Montagem do Layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)       # Espaço entre os elementos
        self.layout.setContentsMargins(20, 20, 20, 20) # Margens da janela

        # --- Título ---
        self.label_titulo = QLabel("Suas Tarefas")
        self.label_titulo.setObjectName("Titulo") # Para o CSS identificar
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_titulo)

        # --- Campo de Texto ---
        self.input_tarefa = QLineEdit()
        self.input_tarefa.setPlaceholderText("O que precisa ser feito hoje?")
        self.layout.addWidget(self.input_tarefa)

        # --- Botão Adicionar ---
        self.btn_adicionar = QPushButton("➕ Adicionar Nova Tarefa")
        self.btn_adicionar.setCursor(Qt.PointingHandCursor) # Mãozinha do mouse
        self.btn_adicionar.clicked.connect(self.adicionar_tarefa)
        self.layout.addWidget(self.btn_adicionar)

        # --- Lista de Tarefas ---
        self.lista_widget = QListWidget()
        self.layout.addWidget(self.lista_widget)

        # --- Botão Remover ---
        self.btn_remover = QPushButton("🗑️ Excluir Selecionada")
        self.btn_remover.setCursor(Qt.PointingHandCursor)
        # Sobrescreve o estilo apenas deste botão para cinza escuro
        self.btn_remover.setStyleSheet("""
            QPushButton {
                background-color: #2b2d42; 
                border: 2px solid #ef233c;
            }
            QPushButton:hover {
                background-color: #ef233c;
            }
        """)
        self.btn_remover.clicked.connect(self.remover_tarefa)
        self.layout.addWidget(self.btn_remover)

        # Finaliza layout
        self.setLayout(self.layout)
        
        # Carrega os dados
        self.atualizar_lista()

    def adicionar_tarefa(self):
        descricao = self.input_tarefa.text()
        if not descricao:
            return # Apenas ignora se estiver vazio, fica mais fluido
        
        try:
            self.sistema.registrar_tarefa(descricao)
            self.input_tarefa.clear()
            self.atualizar_lista()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro: {e}")

    def atualizar_lista(self):
        self.lista_widget.clear()
        tarefas = self.sistema.obter_todas_tarefas()
        
        for t in tarefas:
            # Adiciona ícone de bolinha antes do texto
            item = QListWidgetItem(f" •  {t.descricao}")
            item.setData(Qt.UserRole, t.id)
            
            # Fonte levemente maior para a lista
            font = QFont()
            font.setPointSize(12)
            item.setFont(font)
            
            self.lista_widget.addItem(item)

    def remover_tarefa(self):
        item_selecionado = self.lista_widget.currentItem()
        if not item_selecionado:
            return

        id_tarefa = item_selecionado.data(Qt.UserRole)
        self.sistema.excluir_tarefa(id_tarefa)
        self.atualizar_lista()
        
        # Feedback visual na barra de status (opcional, aqui uso print para simplificar)
        print("Tarefa concluída!")

    def closeEvent(self, event):
        self.sistema.encerrar_sistema()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())
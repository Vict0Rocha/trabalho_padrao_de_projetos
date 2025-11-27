# 📋 Gerenciador de Tarefas (ToDo List)

Este projeto é uma aplicação de linha de comando (CLI) desenvolvida em **Python** para gerenciamento de tarefas. O objetivo principal deste projeto não é apenas a funcionalidade, mas a demonstração prática de **Arquitetura de Software** e aplicação de **Padrões de Projeto (Design Patterns - GoF)** para criar um sistema escalável, organizado e desacoplado.

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Banco de Dados:** SQLite3 (Nativo)
* **Paradigma:** Orientação a Objetos (POO)

## 🏗️ Padrões de Projeto Implementados

O sistema utiliza uma combinação de padrões do **GoF (Gang of Four)** e padrões de **Arquitetura Enterprise**:

1.  **Singleton:** Garante uma única instância de conexão com o Banco de Dados.
2.  **Factory Method:** Centraliza e encapsula a regra de criação de objetos.
3.  **Facade:** Simplifica a interface do sistema, escondendo a complexidade do banco e das regras de negócio do usuário final (Main).
4.  **DAO (Data Access Object):** Separa a lógica de persistência (SQL) da lógica de negócio.
5.  **Model / DTO:** Representa os dados como objetos puros.

---

## 📂 Estrutura do Projeto

A organização dos arquivos segue o princípio da **Separação de Responsabilidades (SoC)**:

```text
MeuProjeto/
│
├── database.py   # SINGLETON - Gerencia a conexão única com SQLite
├── model.py      # MODEL - Define a classe 'Tarefa' (atributos)
├── dao.py        # DAO - Executa comandos SQL (Insert, Select, Delete)
├── factory.py    # FACTORY - Fábrica para instanciar novas tarefas
├── facade.py     # FACADE - Fachada que coordena todos os subsistemas
└── main.py       # CLIENT - Interface de interação com o usuário (Menu
```

## 🧠 Detalhamento da Arquitetura
1. Database (Singleton)
  Arquivo: database.py
  Função: Evitar múltiplas conexões desnecessárias ao arquivo do banco.
  Como funciona: Utiliza o método __new__ para verificar se já existe uma instância ativa. Se existir, retorna a mesma; se não, cria uma nova.

2. DAO (Data Access Object)
  Arquivo: dao.py
  Função: Abstrair o SQL.
  Detalhe: O DAO solicita a instância do Singleton para executar queries. É aqui que o ID é gerado automaticamente pelo banco (AUTOINCREMENT).

3. Factory Method
  Arquivo: factory.py
  Função: Criar objetos Tarefa.
  Justificativa: Se no futuro a regra de criação mudar (ex: validar se a descrição tem no mínimo 5 letras), a alteração é feita apenas na fábrica, sem quebrar o restante do código.

4. Facade (Fachada)
  Arquivo: facade.py
  Função: É o "porteiro" do sistema.
  Benefício: O arquivo main.py não sabe que existe SQL ou Banco de Dados. Ele apenas pede: sistema.registrar_tarefa(). O Facade coordena a Fábrica e o DAO para realizar o pedido.


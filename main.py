# Arquivo: main.py
import sys
from facade import SistemaTarefasFacade

def menu():
    # Inicializa a Fachada
    sistema = SistemaTarefasFacade()

    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1 - ADICIONAR TAREFA")
        print("2 - LISTAR TAREFAS")
        print("3 - EXCLUIR TAREFA")
        print("0 - SAIR")
        
        opcao = input("Escolha uma opção <<< ")

        if opcao == "1":
            desc = input("Digite a descrição da tarefa <<< ")
            try:
                sistema.registrar_tarefa(desc)
            except ValueError as e:
                print(f"[Erro]: {e}")

        elif opcao == "2":
            tarefas = sistema.obter_todas_tarefas()
            print("\n--- Lista ---")
            for t in tarefas:
                print(f"[{t.id}] {t.descricao}")

        elif opcao == "3":
            try:
                id_t = int(input("Qual ID apagar? <<< "))
                sistema.excluir_tarefa(id_t)
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "0":
            sistema.encerrar_sistema()
            sys.exit()
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
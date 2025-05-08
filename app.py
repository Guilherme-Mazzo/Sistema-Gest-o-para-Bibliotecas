# app.py
import livros
import cliente
import emprestimo_devolucao

def mostrar_menu():
    while True:
        print("\n======= SISTEMA DE BIBLIOTECA =======")
        print("[1] Cadastrar livro")
        print("[2] Cadastrar usuário")
        print("[3] Realizar empréstimo")
        print("[4] Devolver livro")
        print("[5] Listar livros disponíveis")
        print("[6] Listar livros emprestados")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            livros.menu_livros()
        elif opcao == "2":
            cliente.menu_cliente()
        elif opcao == "3":
            emprestimo_devolucao.menu_emprestimo()
        elif opcao == "4":
            emprestimo_devolucao.menu_devolucao()
        elif opcao == "5":
            print("\nLivros disponíveis:")
            for livro in livros.lista_livros:
                if livro.get("disponivel", True):
                    print(livro)
        elif opcao == "6":
            print("\nLivros emprestados:")
            for livro in livros.lista_livros:
                if not livro.get("disponivel", True):
                    print(livro)
        elif opcao == "0":
            print("Saindo do sistema!")
            break
        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    livros.carregar_livros()
    cliente.carregar_usuarios()
    emprestimo_devolucao.carregar_emprestimos()
    mostrar_menu()

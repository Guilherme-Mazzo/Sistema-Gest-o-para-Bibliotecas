# emprestimo_devolucao.py
import json
import os
import livros

CAMINHO_ARQUIVO_EMPRESTIMOS = "data/emprestimos.json"
lista_emprestimos = []

def carregar_emprestimos():
    global lista_emprestimos
    if os.path.exists(CAMINHO_ARQUIVO_EMPRESTIMOS):
        with open(CAMINHO_ARQUIVO_EMPRESTIMOS, "r", encoding="utf-8") as f:
            lista_emprestimos = json.load(f)

def salvar_emprestimos():
    with open(CAMINHO_ARQUIVO_EMPRESTIMOS, "w", encoding="utf-8") as f:
        json.dump(lista_emprestimos, f, indent=4, ensure_ascii=False)

def menu_emprestimo():
    isbn = input("Digite o ISBN do livro a ser emprestado: ")
    cliente_id = input("Digite o ID do Cliente: ")

    for livro in livros.lista_livros:
        if livro["isbn"] == isbn:
            if livro.get("disponivel", True):
                livro["disponivel"] = False
                lista_emprestimos.append({
                    "isbn": isbn,
                    "cliente_id": cliente_id
                })
                salvar_emprestimos()
                livros.salvar_livros()
                print("Livro emprestado com sucesso!")
                return
            else:
                print("Livro já está emprestado.")
                return

    print("Livro não encontrado.")

def menu_devolucao():
    isbn = input("Digite o ISBN do livro a ser devolvido: ")

    for livro in livros.lista_livros:
        if livro["isbn"] == isbn:
            if not livro.get("disponivel", True):
                livro["disponivel"] = True
                for emprestimo in lista_emprestimos:
                    if emprestimo["isbn"] == isbn:
                        lista_emprestimos.remove(emprestimo)
                        break
                salvar_emprestimos()
                livros.salvar_livros()
                print("Livro devolvido com sucesso!")
                return
            else:
                print("Este livro já está disponível.")
                return

    print("Livro não encontrado.")

if __name__ == "__main__":
    carregar_emprestimos()
    menu_devolucao()
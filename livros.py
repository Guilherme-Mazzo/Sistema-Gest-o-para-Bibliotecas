import json
import os

CAMINHO_ARQUIVO_LIVROS = "data/livros.json"
lista_livros = []

# Carregar livros do arquivo ao iniciar
def carregar_livros():
    global lista_livros
    if os.path.exists(CAMINHO_ARQUIVO_LIVROS):
        with open(CAMINHO_ARQUIVO_LIVROS, "r", encoding="utf-8") as f:
            lista_livros = json.load(f)

# Salvar livros no arquivo após cada alteração
def salvar_livros():
    with open(CAMINHO_ARQUIVO_LIVROS, "w", encoding="utf-8") as f:
        json.dump(lista_livros, f, indent=4, ensure_ascii=False)

# Função que vai pegar os dados dos inputs e armazenar dentro da lista_livros
def cadastrar_livro(nome_livro, isbn, autor, categoria):
    lista_cadastro_livro = {
        "nome_livro" : nome_livro,
        "isbn" : isbn,
        "autor" : autor,
        "categoria": categoria,
        "disponivel": True
    }
    lista_livros.append(lista_cadastro_livro)
    salvar_livros()  # Salva automaticamente após cadastrar

# Função que vai criar o menu livro
def menu_livros():
    while True:
        nome_livro = input("Digite o nome do livro: ")
        isbn = input("Numero do ISBN: ")
        autor = input("Autor do livro: ")
        categoria = input("Qual a categoria do livro: ")

        cadastrar_livro(nome_livro, isbn, autor, categoria)  # Vai executar a função cadastrar_livro

        print("Livro cadastrado com sucesso!")

        continuar = input("Desejar cadastrar outro livro?    [s/n] ").lower()
        if continuar != 's':
            break

def listar_livros_disponiveis():
    print("\nLivros disponíveis:")
    for livro in lista_livros:
        if livro.get("disponivel", True):
            print(livro)

if __name__ == "__main__":
    menu_livros()
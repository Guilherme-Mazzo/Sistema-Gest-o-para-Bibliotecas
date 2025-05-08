import tkinter as tk
from tkinter import messagebox, simpledialog
import livros
import cliente
import emprestimo_devolucao

# Carregar dados ao iniciar a aplicação
livros.carregar_livros()
cliente.carregar_usuarios()
emprestimo_devolucao.carregar_emprestimos()

# Funções para as operações


def cadastrar_livro():
    nome = simpledialog.askstring("Cadastro de Livro", "Nome do Livro:")
    isbn = simpledialog.askstring("Cadastro de Livro", "ISBN:")
    autor = simpledialog.askstring("Cadastro de Livro", "Autor:")
    categoria = simpledialog.askstring("Cadastro de Livro", "Categoria:")
    if nome and isbn:
        livros.cadastrar_livro(nome, isbn, autor, categoria)
        livros.salvar_livros()
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")


def cadastrar_usuario():
    id_cliente = simpledialog.askstring(
        "Cadastro de Cliente", "ID do Cliente:")
    nome = simpledialog.askstring("Cadastro de Cliente", "Nome:")
    telefone = simpledialog.askstring("Cadastro de Cliente", "Telefone:")
    email = simpledialog.askstring("Cadastro de Cliente", "Email:")
    cpf = simpledialog.askstring("Cadastro de Cliente", "CPF:")
    endereco = simpledialog.askstring("Cadastro de Cliente", "Endereço:")
    cidade = simpledialog.askstring("Cadastro de Cliente", "Cidade:")
    if id_cliente and nome:
        cliente.cadastrar_cliente(
            id_cliente, nome, telefone, email, cpf, endereco, cidade)
        cliente.salvar_usuarios()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")


def emprestar_livro():
    isbn = simpledialog.askstring("Empréstimo", "ISBN do livro:")
    cliente_id = simpledialog.askstring("Empréstimo", "ID do Cliente:")
    emprestimo_devolucao.realizar_emprestimo(isbn, cliente_id)


def devolver_livro():
    isbn = simpledialog.askstring("Devolução", "ISBN do livro:")
    emprestimo_devolucao.realizar_devolucao(isbn)


def listar_livros_disponiveis():
    livros_disp = [
        livro for livro in livros.lista_livros if livro.get("disponivel", True)]
    texto = "\n".join(
        [f"{livro['nome_livro']} ({livro['isbn']})" for livro in livros_disp]) or "Nenhum livro disponível."
    messagebox.showinfo("Livros Disponíveis", texto)


def listar_livros_emprestados():
    livros_emp = [
        livro for livro in livros.lista_livros if not livro.get("disponivel", True)]
    texto = "\n".join(
        [f"{livro['nome_livro']} ({livro['isbn']})" for livro in livros_emp]) or "Nenhum livro emprestado."
    messagebox.showinfo("Livros Emprestados", texto)


# Interface principal
janela = tk.Tk()
janela.title("Sistema de Biblioteca")
janela.geometry("400x400")

# Botões do menu
botoes = [
    ("Cadastrar Livro", cadastrar_livro),
    ("Cadastrar Cliente", cadastrar_usuario),
    ("Realizar Empréstimo", emprestar_livro),
    ("Devolver Livro", devolver_livro),
    ("Listar Livros Disponíveis", listar_livros_disponiveis),
    ("Listar Livros Emprestados", listar_livros_emprestados),
    ("Sair", janela.quit)
]

for texto, comando in botoes:
    tk.Button(janela, text=texto, width=30, command=comando).pack(pady=5)

janela.mainloop()

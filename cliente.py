'''
global lista_usuarios
O que faz: A palavra-chave global é usada para declarar que a variável lista_usuarios que está sendo manipulada dentro da função carregar_usuarios()
é a mesma variável lista_usuarios que foi definida no início do módulo (fora da função).

Por que é necessário: Quando você usa a palavra-chave global, está dizendo ao Python para modificar a variável global diretamente, em vez de criar uma nova variável local dentro da função. 
Isso é importante porque queremos que a função modifique a lista global de usuários e não apenas uma cópia local dela

with open(CAMINHO_ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
O que faz: A função open() abre o arquivo no modo de leitura ("r"). O argumento encoding="utf-8" garante que o arquivo será lido usando a codificação de caracteres UTF-8,
o que é importante para suportar caracteres especiais (acentos, ç, etc.).

Por que é necessário: O arquivo precisa ser aberto em modo de leitura para que possamos acessar seu conteúdo. Usando o contexto with open(...)
 as f, garantimos que o arquivo será fechado automaticamente após a execução do bloco de código, evitando possíveis erros e vazamentos de recursos.

'''




import json
import os

CAMINHO_ARQUIVO_USUARIOS = "data/cliente.json"
lista_usuarios = []

# Carregar usuários do arquivo ao iniciar
def carregar_usuarios():
    global lista_usuarios
    if os.path.exists(CAMINHO_ARQUIVO_USUARIOS):
        with open(CAMINHO_ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            lista_usuarios = json.load(f)

# Salvar usuários no arquivo após cada alteração
def salvar_usuarios():
    with open(CAMINHO_ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(lista_usuarios, f, indent=4, ensure_ascii=False)

# Lista que vai armazenar informações dos novos clientes
lista_clientes = []

# Função que vai pegar as informações dos inputs e armazenar dentro da lista_clientes
def cadastrar_cliente(id_cliente, nome_cliente, telefone, email, cpf, endereco, cidade):
    cliente = {
        "id_cliente": id_cliente,
        "nome_cliente": nome_cliente,
        "telefone": telefone,
        "email": email,
        "cpf": cpf,
        "endereco": endereco,
        "cidade": cidade
    }
    lista_clientes.append(cliente)
    lista_usuarios.append(cliente)
    salvar_usuarios()

# Função que mostra as informações do menu interativo
def menu_cliente():
    carregar_usuarios()

    while True:
        id_cliente = input("Digite o ID do cliente: ")
        nome_cliente = input("Digite o nome do cliente: ")
        telefone = input("Digite um número para contato: ")
        email = input("Digite o email: ")
        cpf = input("Digite o CPF: ")
        endereco = input("Digite o endereço residencial: ")
        cidade = input("Qual é a cidade: ")

        cadastrar_cliente(id_cliente, nome_cliente, telefone, email, cpf, endereco, cidade)

        continuar = input("Deseja cadastrar outro cliente? [s/n] ").lower()
        if continuar != 's':
            break

    print("\nLista de clientes cadastrados:")
    for cliente in lista_clientes:
        print(cliente)

if __name__ == "__main__":
    menu_cliente()

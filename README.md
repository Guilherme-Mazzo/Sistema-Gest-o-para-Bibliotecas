# 📚 Sistema de Gerenciamento de Biblioteca

Este projeto é um sistema de gerenciamento de biblioteca feito em **Python**, dividido em múltiplos módulos, com suporte para **interface gráfica (GUI)** usando `tkinter`. Ele permite cadastrar livros, gerenciar clientes, realizar empréstimos e devoluções, e salvar os dados em arquivos JSON.

## 🔧 Funcionalidades

✅ Cadastro de Livros  
✅ Cadastro de Clientes  
✅ Empréstimos de Livros  
✅ Devolução de Livros  
✅ Armazenamento persistente em arquivos JSON  
✅ Interface Gráfica com Tkinter  
✅ Menu Interativo via terminal (modo CLI também disponível)

---

## 📁 Estrutura do Projeto

biblioteca/
│
├── app.py # Menu principal via terminal
├── interface.py # Interface gráfica com tkinter
├── cliente.py # Cadastro e gerenciamento de clientes
├── livros.py # Cadastro e gerenciamento de livros
├── emprestimo_devolucao.py # Lógica de empréstimos e devoluções
├── data/
│ ├── cliente.json # Armazena os dados dos clientes
│ ├── livros.json # Armazena os dados dos livros
│ └── emprestimos.json # Armazena os dados dos empréstimos
├── README.md # Este arquivo
└── apostila.pdf # Apostila completa explicando o sistema


---

## 🖥️ Interface Gráfica

A interface gráfica foi desenvolvida com o `tkinter` e substitui a necessidade de utilizar o terminal. Através dela, é possível realizar:

- Cadastro de livros e clientes através de formulários simples.
- Visualização de livros disponíveis e emprestados.
- Empréstimos e devoluções com apenas um clique.

### 🧪 Como executar a interface:


python interface.py
🧠 Conhecimentos Aplicados
Este projeto abrange os seguintes tópicos:

Manipulação de arquivos JSON

Estrutura modular em Python

Funções, listas e dicionários

Interface gráfica com tkinter

Validação de dados

Menu interativo em CLI

Organização de código e boas práticas



🚀 Requisitos para rodar o projeto
Python 3.10 ou superior

Não é necessário instalar bibliotecas externas, pois todas as utilizadas são nativas do Python.

🤝 Contribuição
Sinta-se livre para sugerir melhorias, abrir issues ou fazer um fork para expandir a funcionalidade. Este projeto pode ser um excelente ponto de partida para sistemas mais robustos, com banco de dados e autenticação.

👤 Autor
Guilherme
📧 Desenvolvedor em formação na área de Análise de Dados
🔗 GitHub: github.com/seu-usuario

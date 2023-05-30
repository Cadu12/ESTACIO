import tkinter as tk
from tkinter import messagebox
import sqlite3

def criar_tabela_usuarios():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, senha TEXT NOT NULL)')
    conn.commit()
    conn.close()

def criar_tabela_produtos():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco REAL NOT NULL)')
    conn.commit()
    conn.close()

def fazer_login():
    nome = entry_nome.get()
    senha = entry_senha.get()

    if nome and senha:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE nome=? AND senha=?', (nome, senha))
        usuario = cursor.fetchone()
        conn.close()

        if usuario is not None:
            tela_login.destroy()
            tela_produtos()
        else:
            messagebox.showerror('Erro', 'Nome de usuário ou senha incorretos')
    else:
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos')

def cadastrar_usuario():
    nome = entry_nome_cadastro.get()
    senha = entry_senha_cadastro.get()

    if nome and senha:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE nome=?', (nome,))
        usuario = cursor.fetchone()

        if usuario is not None:
            conn.close()
            messagebox.showerror('Erro', 'Usuário já existe')
        else:
            cursor.execute('INSERT INTO usuarios (nome, senha) VALUES (?, ?)', (nome, senha))
            conn.commit()
            conn.close()

            messagebox.showinfo('Sucesso', 'Usuário cadastrado com sucesso')
    else:
        messagebox.showerror('Erro', 'Por favor, preencha todos os campos')

def tela_produtos():
    def atualizar_lista_produtos():
        lista_produtos.delete(0, tk.END)

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        conn.close()

        for produto in produtos:
            lista_produtos.insert(tk.END, f"{produto[1]} - preço: R$ {produto[2]:.2f}")

    def cadastrar_produto():
        nome = entry_nome_produto.get()
        preco = float(entry_preco_produto.get())

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, preco))
        conn.commit()
        conn.close()

        atualizar_lista_produtos()
        messagebox.showinfo('Sucesso', 'Produto cadastrado com sucesso')

    # Função para alterar o produto selecionado
    def alterar_produto():
        item_selecionado = lista_produtos.curselection()
        if item_selecionado:
            nome = entry_nome_produto.get()
            preco = float(entry_preco_produto.get())

            conn = sqlite3.connect('banco.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE produtos SET nome=?, preco=? WHERE id=?', (nome, preco, item_selecionado[0] + 1))
            conn.commit()
            conn.close()

            atualizar_lista_produtos()
            messagebox.showinfo('Sucesso', 'Produto alterado com sucesso')
        else:
            messagebox.showerror('Erro', 'Nenhum produto selecionado')

    # Função para excluir o produto selecionado
    def excluir_produto():
        item_selecionado = lista_produtos.curselection()
        if item_selecionado:
            conn = sqlite3.connect('banco.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM produtos WHERE id=?', (item_selecionado[0] + 1,))
            conn.commit()
            conn.close()

            atualizar_lista_produtos()
            messagebox.showinfo('Sucesso', 'Produto excluído com sucesso')
        else:
            messagebox.showerror('Erro', 'Nenhum produto selecionado')

    tela_produtos = tk.Tk()
    tela_produtos.title('Cadastro de Produtos')

    label_nome_produto = tk.Label(tela_produtos, text='Nome do Produto:')
    label_nome_produto.pack()
    entry_nome_produto = tk.Entry(tela_produtos)
    entry_nome_produto.pack()

    label_preco_produto = tk.Label(tela_produtos, text='Preço do Produto:')
    label_preco_produto.pack()
    entry_preco_produto = tk.Entry(tela_produtos)
    entry_preco_produto.pack()

    button_cadastrar_produto = tk.Button(tela_produtos, text='Cadastrar Produto', command=cadastrar_produto)
    button_cadastrar_produto.pack()

    button_alterar_produto = tk.Button(tela_produtos, text='Alterar Produto', command=alterar_produto)
    button_alterar_produto.pack()

    button_excluir_produto = tk.Button(tela_produtos, text='Excluir Produto', command=excluir_produto)
    button_excluir_produto.pack()

    lista_produtos = tk.Listbox(tela_produtos)
    lista_produtos.pack()

    atualizar_lista_produtos()

    tela_produtos.mainloop()

# Criação da tela de login
tela_login = tk.Tk()
tela_login.title('Login')

label_nome = tk.Label(tela_login, text='Nome de usuário:')
label_nome.pack()
entry_nome = tk.Entry(tela_login)
entry_nome.pack()

label_senha = tk.Label(tela_login, text='Senha:')
label_senha.pack()
entry_senha = tk.Entry(tela_login, show='*')
entry_senha.pack()

button_login = tk.Button(tela_login, text='Login', command=fazer_login)
button_login.pack()

label_cadastro = tk.Label(tela_login, text='Cadastre-se:')
label_cadastro.pack()

label_nome_cadastro = tk.Label(tela_login, text='Nome de usuário:')
label_nome_cadastro.pack()
entry_nome_cadastro = tk.Entry(tela_login)
entry_nome_cadastro.pack()

label_senha_cadastro = tk.Label(tela_login, text='Senha:')
label_senha_cadastro.pack()
entry_senha_cadastro = tk.Entry(tela_login, show='*')
entry_senha_cadastro.pack()

button_cadastrar = tk.Button(tela_login, text='Cadastrar', command=cadastrar_usuario)
button_cadastrar.pack()

criar_tabela_usuarios()
criar_tabela_produtos()

tela_login.mainloop()

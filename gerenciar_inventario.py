import tkinter as tk
from tkinter import ttk, messagebox
from models.inventario import Inventario  

class GerenciarInventario:
    def __init__(self, master, inventario):
        self.master = master  # Janela principal do aplicativo
        self.master.title("Gerenciar Inventário")  # Define o título da janela
        self.inventario = inventario  # Objeto de inventário que será gerenciado

        self.create_widgets()  # Chamada do método para criar os widgets na interface

    def create_widgets(self):
        # Cria um frame na janela principal para organizar os widgets
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)  # Empacota o frame com espaçamento

        # Cria e posiciona um label e um campo de entrada para o nome do item
        tk.Label(self.frame, text="Item:").grid(row=0, column=0, pady=5)
        self.entry_item = tk.Entry(self.frame)
        self.entry_item.grid(row=0, column=1, pady=5)

        # Cria e posiciona um label e um campo de entrada para a quantidade do item
        tk.Label(self.frame, text="Quantidade:").grid(row=1, column=0, pady=5)
        self.entry_quantidade = tk.Entry(self.frame)
        self.entry_quantidade.grid(row=1, column=1, pady=5)

        # Cria e posiciona botões para adicionar, remover e listar os itens
        tk.Button(self.frame, text="Adicionar Item", command=self.adicionar_item).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.frame, text="Remover Item", command=self.remover_item).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Itens", command=self.listar_itens).grid(row=4, columnspan=2, pady=10)

    def adicionar_item(self):
        # Adiciona um item ao inventário após validar a entrada
        item = self.entry_item.get()
        try:
            quantidade = int(self.entry_quantidade.get())  # Tenta converter a entrada de quantidade para inteiro
            self.inventario.adicionar_item(item, quantidade)
            messagebox.showinfo("Sucesso", "Item adicionado com sucesso.")
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida. Por favor, insira um número inteiro.")

    def remover_item(self):
        # Remove um item do inventário
        item = self.entry_item.get()
        try:
            quantidade = int(self.entry_quantidade.get())  # Tenta converter a entrada de quantidade para inteiro
            self.inventario.remover_item(item, quantidade)
            messagebox.showinfo("Sucesso", "Item removido com sucesso.")
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida. Por favor, insira um número inteiro.")

    def listar_itens(self):
        # Lista todos os itens do inventário
        itens_info = self.inventario.listar_itens()
        messagebox.showinfo("Itens no Inventário", itens_info)
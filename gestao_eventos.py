import tkinter as tk
from tkinter import messagebox
from models.evento import Evento  

class GestaoEventos:
    def __init__(self, master, eventos):
        self.master = master  # Janela principal do aplicativo
        self.eventos = eventos  # Lista de eventos
        self.master.title("Gestão de Eventos")  # Define o título da janela

        self.create_widgets()  # Chamada do método para criar os widgets na interface

    def create_widgets(self):
        # Cria um frame na janela principal para organizar os widgets
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)  # Empacota o frame com espaçamento

        # Cria e posiciona um label e um campo de entrada para o nome do evento
        tk.Label(self.frame, text="Nome do Evento:").grid(row=0, column=0, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        # Cria e posiciona um label e um campo de entrada para a data do evento
        tk.Label(self.frame, text="Data do Evento:").grid(row=1, column=0, pady=5)
        self.entry_data = tk.Entry(self.frame)
        self.entry_data.grid(row=1, column=1, pady=5)

        # Cria e posiciona um label e um campo de entrada para o local do evento
        tk.Label(self.frame, text="Local do Evento:").grid(row=2, column=0, pady=5)
        self.entry_local = tk.Entry(self.frame)
        self.entry_local.grid(row=2, column=1, pady=5)

        # Cria e posiciona botões para adicionar, listar e remover eventos
        tk.Button(self.frame, text="Adicionar Evento", command=self.adicionar_evento).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Eventos", command=self.listar_eventos).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.frame, text="Remover Evento", command=self.remover_evento).grid(row=5, columnspan=2, pady=10)

    def adicionar_evento(self):
        # Adiciona um evento à lista
        nome = self.entry_nome.get()
        data = self.entry_data.get()
        local = self.entry_local.get()

        if nome and data and local:
            self.eventos.adicionar_evento(nome, data, local)
            messagebox.showinfo("Sucesso", "Evento adicionado com sucesso")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def listar_eventos(self):
        # Lista todos os eventos
        eventos_info = self.eventos.listar_eventos()
        messagebox.showinfo("Eventos", eventos_info)

    def remover_evento(self):
        # Remove um evento da lista com base no nome fornecido
        nome = self.entry_nome.get()

        if nome:
            self.eventos.remover_evento(nome)
            messagebox.showinfo("Sucesso", "Evento removido com sucesso")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Nome do evento deve ser preenchido.")

    def limpar_campos(self):
        # Limpa os campos de entrada após a adição ou remoção de um evento
        self.entry_nome.delete(0, tk.END)
        self.entry_data.delete(0, tk.END)
        self.entry_local.delete(0, tk.END)
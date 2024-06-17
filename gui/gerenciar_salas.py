import tkinter as tk
from tkinter import messagebox
from models.sala import Sala

class GerenciarSalas:
    def __init__(self, master, salas):
        self.master = master  # Janela principal do aplicativo
        self.salas = salas  # Lista de salas
        self.master.title("Gerenciar Salas")  # Define o título da janela

        self.create_widgets()  # Chamada do método para criar os widgets na interface

    def create_widgets(self):
        # Cria um frame na janela principal para organizar os widgets
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)  # Empacota o frame com espaçamento

        # Cria e posiciona um label e um campo de entrada para o número da sala
        tk.Label(self.frame, text="Número da Sala:").grid(row=0, column=0, pady=5)
        self.entry_numero = tk.Entry(self.frame)
        self.entry_numero.grid(row=0, column=1, pady=5)

        # Cria e posiciona um label e um campo de entrada para a capacidade da sala
        tk.Label(self.frame, text="Capacidade:").grid(row=1, column=0, pady=5)
        self.entry_capacidade = tk.Entry(self.frame)
        self.entry_capacidade.grid(row=1, column=1, pady=5)

        # Cria e posiciona botões para adicionar, listar, editar e remover salas
        tk.Button(self.frame, text="Adicionar Sala", command=self.adicionar_sala).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Salas", command=self.listar_salas).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame, text="Editar Sala", command=self.editar_sala).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.frame, text="Remover Sala", command=self.remover_sala).grid(row=5, columnspan=2, pady=10)

    def adicionar_sala(self):
        # Adiciona uma sala à lista após validar a entrada
        numero = self.entry_numero.get()
        try:
            capacidade = int(self.entry_capacidade.get())
            if capacidade <= 0:
                raise ValueError("A capacidade deve ser um número positivo.")
            sala = Sala(numero, capacidade)
            self.salas.append(sala)
            messagebox.showinfo("Sucesso", "Sala adicionada com sucesso")
            self.limpar_campos()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def editar_sala(self):
        # Edita a capacidade de uma sala existente
        numero = self.entry_numero.get()
        sala = next((s for s in self.salas if s.numero == numero), None)
        if sala:
            try:
                nova_capacidade = int(self.entry_capacidade.get())
                if nova_capacidade <= 0:
                    raise ValueError("A capacidade deve ser um número positivo.")
                sala.capacidade = nova_capacidade
                messagebox.showinfo("Sucesso", "Informações da sala atualizadas com sucesso.")
                self.limpar_campos()
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showerror("Erro", "Sala não encontrada.")

    def remover_sala(self):
        # Remove uma sala da lista com base no número fornecido
        numero = self.entry_numero.get()
        sala = next((s for s in self.salas if s.numero == numero), None)
        if sala:
            self.salas.remove(sala)
            messagebox.showinfo("Sucesso", "Sala removida com sucesso.")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Sala não encontrada.")

    def listar_salas(self):
        # Lista todas as salas
        salas_info = "\n".join([sala.exibir_informacoes() for sala in self.salas])
        messagebox.showinfo("Lista de Salas", salas_info)

    def limpar_campos(self):
        # Limpa os campos de entrada após a adição, edição ou remoção de uma sala
        self.entry_numero.delete(0, tk.END)
        self.entry_capacidade.delete(0, tk.END)

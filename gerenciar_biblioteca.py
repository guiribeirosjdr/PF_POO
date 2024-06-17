import tkinter as tk
from tkinter import ttk, messagebox

class GerenciarBiblioteca:
    def __init__(self, master, biblioteca, alunos):
        self.master = master  # Janela principal da aplicação.
        self.biblioteca = biblioteca  # Instância da classe Biblioteca que gerencia os livros.
        self.alunos = alunos  # Lista de alunos (objetos).
        self.create_widgets()  # Método para criar e configurar widgets.

    def create_widgets(self):
        # Configuração dos componentes da interface gráfica.
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)  # Empacotamento com padding.

        # Campo de entrada para o nome do livro.
        tk.Label(self.frame, text="Livro:").grid(row=0, column=0, pady=5)
        self.entry_livro = tk.Entry(self.frame)
        self.entry_livro.grid(row=0, column=1, pady=5)

        # Botões para adicionar e remover livros, e listar todos os livros.
        tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro).grid(row=1, columnspan=2, pady=10)
        tk.Button(self.frame, text="Remover Livro", command=self.remover_livro).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Livros", command=self.listar_livros).grid(row=3, columnspan=2, pady=10)

        # Combobox para selecionar um aluno para reserva de livro.
        tk.Label(self.frame, text="Aluno:").grid(row=4, column=0, pady=5)
        self.combo_aluno = ttk.Combobox(self.frame, values=[aluno.nome for aluno in self.alunos])
        self.combo_aluno.grid(row=4, column=1, pady=5)

        # Botões para reservar e excluir reservas de livros.
        tk.Button(self.frame, text="Reservar Livro", command=self.reservar_livro).grid(row=5, columnspan=2, pady=10)
        tk.Button(self.frame, text="Excluir Reserva", command=self.excluir_reserva).grid(row=7, columnspan=2, pady=10)

    def adicionar_livro(self):
        # Adiciona um livro à biblioteca e mostra uma mensagem de sucesso.
        livro = self.entry_livro.get()
        self.biblioteca.adicionar_livro(livro)
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso.")

    def remover_livro(self):
        # Remove um livro da biblioteca e mostra uma mensagem de sucesso.
        livro = self.entry_livro.get()
        self.biblioteca.remover_livro(livro)
        messagebox.showinfo("Sucesso", "Livro removido com sucesso.")

    def listar_livros(self):
        # Lista todos os livros na biblioteca e mostra em uma messagebox.
        livros_info = self.biblioteca.listar_livros()
        messagebox.showinfo("Livros", livros_info)

    def reservar_livro(self):
        # Reserva um livro para um aluno e mostra uma mensagem de sucesso ou erro.
        livro = self.entry_livro.get()
        aluno_nome = self.combo_aluno.get()
        aluno = next((aluno for aluno in self.alunos if aluno.nome == aluno_nome), None)

        if aluno:
            self.biblioteca.reservar_livro(livro, aluno)
            messagebox.showinfo("Sucesso", "Livro reservado com sucesso.")
        else:
            messagebox.showwarning("Erro", "Selecione um aluno válido.")

    def excluir_reserva(self):
        # Exclui uma reserva de livro e mostra uma mensagem de sucesso ou erro.
        livro = self.entry_livro.get()
        aluno_nome = self.combo_aluno.get()
        aluno = next((aluno for aluno in self.alunos if aluno.nome == aluno_nome), None)

        if aluno:
            self.biblioteca.excluir_reserva(livro, aluno)
            messagebox.showinfo("Sucesso", "Reserva excluída com sucesso.")
        else:
            messagebox.showwarning("Erro", "Selecione um aluno válido.")

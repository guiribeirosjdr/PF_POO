import tkinter as tk
from tkinter import messagebox
from models.aluno import Aluno  

class GerenciarAlunos:
    def __init__(self, master, alunos):
        self.master = master  # Janela principal do aplicativo.
        self.master.title("Gerenciar Alunos")  # Define o título da janela.
        self.alunos = alunos  # Lista para armazenar os alunos.

        self.create_widgets()  # Chama a função para criar widgets.

    def create_widgets(self):
        # Configuração do layout dos componentes na janela.
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)

        # Criação e posicionamento de labels e entries para nome, idade, matrícula e email do aluno.
        tk.Label(self.frame, text="Nome:").grid(row=0, column=0, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="Idade:").grid(row=1, column=0, pady=5)
        self.entry_idade = tk.Entry(self.frame)
        self.entry_idade.grid(row=1, column=1, pady=5)

        tk.Label(self.frame, text="Matrícula:").grid(row=2, column=0, pady=5)
        self.entry_matricula = tk.Entry(self.frame)
        self.entry_matricula.grid(row=2, column=1, pady=5)

        tk.Label(self.frame, text="E-mail:").grid(row=3, column=0, pady=5)
        self.entry_email = tk.Entry(self.frame)
        self.entry_email.grid(row=3, column=1, pady=5)

        # Botões para adicionar, listar e excluir alunos.
        tk.Button(self.frame, text="Adicionar Aluno", command=self.adicionar_aluno).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Alunos", command=self.listar_alunos).grid(row=5, columnspan=2, pady=10)
        tk.Button(self.frame, text="Excluir Aluno", command=self.excluir_aluno).grid(row=6, columnspan=2, pady=10)

    def adicionar_aluno(self):
        # Adiciona um novo aluno à lista de alunos com as informações fornecidas.
        nome = self.entry_nome.get()
        idade = int(self.entry_idade.get())  # Converte a idade para int.
        matricula = self.entry_matricula.get()
        email = self.entry_email.get()

        aluno = Aluno(nome, idade, matricula, email)  # Cria um objeto aluno.
        self.alunos.append(aluno)  # Adiciona o objeto à lista de alunos.

        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso")

    def listar_alunos(self):
        # Lista todos os alunos registrados.
        alunos_info = "\n".join([aluno.exibir_informacoes() for aluno in self.alunos])
        messagebox.showinfo("Lista de Alunos", alunos_info)

    def excluir_aluno(self):
        # Exclui um aluno com base no nome fornecido.
        nome = self.entry_nome.get()
        for aluno in self.alunos:
            if aluno.nome == nome:
                self.alunos.remove(aluno)
                messagebox.showinfo("Sucesso", f"Aluno {nome} excluído com sucesso.")
                return
        messagebox.showwarning("Atenção", f"Aluno {nome} não encontrado.")

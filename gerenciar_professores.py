import tkinter as tk
from tkinter import ttk, messagebox
from models.professor import Professor  

class GerenciarProfessores:
    def __init__(self, master, professores):
        self.master = master  # Janela principal do aplicativo
        self.master.title("Gerenciar Professores")  # Define o título da janela
        self.professores = professores  # Lista de professores

        self.create_widgets()  # Chamada do método para criar os widgets na interface

    def create_widgets(self):
        # Cria um frame na janela principal para organizar os widgets
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)  # Empacota o frame com espaçamento

        # Cria e posiciona um label e um campo de entrada para o nome do professor
        tk.Label(self.frame, text="Nome:").grid(row=0, column=0, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        # Cria e posiciona um label e um campo de entrada para a idade do professor
        tk.Label(self.frame, text="Idade:").grid(row=1, column=0, pady=5)
        self.entry_idade = tk.Entry(self.frame)
        self.entry_idade.grid(row=1, column=1, pady=5)

        # Cria e posiciona um label e um campo de entrada para as disciplinas do professor
        tk.Label(self.frame, text="Disciplinas:").grid(row=2, column=0, pady=5)
        self.entry_disciplinas = tk.Entry(self.frame)
        self.entry_disciplinas.grid(row=2, column=1, pady=5)

        # Cria e posiciona um label e um campo de entrada para o email do professor
        tk.Label(self.frame, text="Email:").grid(row=3, column=0, pady=5)
        self.entry_email = tk.Entry(self.frame)
        self.entry_email.grid(row=3, column=1, pady=5)

        # Cria e posiciona botões para adicionar, listar e excluir professores
        tk.Button(self.frame, text="Adicionar Professor", command=self.adicionar_professor).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Professores", command=self.listar_professores).grid(row=5, columnspan=2, pady=10)
        tk.Button(self.frame, text="Excluir Professor", command=self.excluir_professor).grid(row=6, columnspan=2, pady=10)

    def adicionar_professor(self):
        # Adiciona um professor à lista após validar a entrada
        nome = self.entry_nome.get()
        try:
            idade = int(self.entry_idade.get())  # Tenta converter a entrada de idade para inteiro
        except ValueError:
            messagebox.showerror("Erro", "Idade inválida. Por favor, insira um número inteiro.")
            return

        disciplinas = self.entry_disciplinas.get().split(",")  # Divide as disciplinas por vírgula
        email = self.entry_email.get()

        if nome and idade > 0 and disciplinas and email:
            professor = Professor(nome, idade, disciplinas, email)
            self.professores.append(professor)
            messagebox.showinfo("Sucesso", "Professor adicionado com sucesso")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente")

    def listar_professores(self):
        # Lista todos os professores
        if self.professores:
            professores_info = "\n".join([professor.exibir_informacoes() for professor in self.professores])
            messagebox.showinfo("Lista de Professores", professores_info)
        else:
            messagebox.showinfo("Lista de Professores", "Nenhum professor cadastrado.")

    def excluir_professor(self):
        # Exclui um professor com base no nome fornecido
        nome = self.entry_nome.get()
        for professor in self.professores:
            if professor.nome == nome:
                self.professores.remove(professor)
                messagebox.showinfo("Sucesso", f"Professor {nome} excluído com sucesso.")
                self.limpar_campos()
                return
        messagebox.showwarning("Atenção", f"Professor {nome} não encontrado.")

    def limpar_campos(self):
        # Limpa os campos de entrada após a adição ou exclusão
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_disciplinas.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)


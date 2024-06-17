import tkinter as tk
from tkinter import messagebox
from models.atividade_extracurricular import AtividadeExtracurricular

class GerenciarAtividadesExtracurriculares:
    def __init__(self, master, atividades_extracurriculares, alunos):
        self.master = master # Janela principal
        self.atividades_extracurriculares = atividades_extracurriculares # Lista de atividades extracurriculares
        self.alunos = alunos # Lista de alunos
        self.master.title("Gerenciar Atividades Extracurriculares")

        self.create_widgets()

    def create_widgets(self):
        # Cria e organiza os widgets na janela
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)

        # Campos para entrada de nome da atividade e seleção de alunos
        tk.Label(self.frame, text="Nome da Atividade:").grid(row=0, column=0, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="Alunos:").grid(row=1, column=0, pady=5)
        self.listbox_alunos = tk.Listbox(self.frame, selectmode=tk.MULTIPLE)
        for aluno in self.alunos:
            self.listbox_alunos.insert(tk.END, aluno.nome)
        self.listbox_alunos.grid(row=1, column=1, pady=5)

        tk.Button(self.frame, text="Adicionar Atividade", command=self.adicionar_atividade).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Atividades", command=self.listar_atividades).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame, text="Excluir Atividade", command=self.excluir_atividade).grid(row=4, columnspan=2, pady=10)

    def adicionar_atividade(self):
        # Adiciona uma nova atividade extracurricular baseada nos inputs do usuário
        nome = self.entry_nome.get()
        alunos_participantes = [self.alunos[int(item)] for item in self.listbox_alunos.curselection()]
        atividade = AtividadeExtracurricular(nome, alunos_participantes)
        self.atividades_extracurriculares.append(atividade)
        messagebox.showinfo("Sucesso", f"Atividade {nome} adicionada com sucesso.")

    def listar_atividades(self):
        # Lista todas as atividades registradas
        atividades_info = "\n".join([atividade.exibir_informacoes() for atividade in self.atividades_extracurriculares])
        messagebox.showinfo("Atividades Extracurriculares", atividades_info)

    def excluir_atividade(self):
        # Exclui uma atividade baseada no nome fornecido
        nome = self.entry_nome.get()
        for atividade in self.atividades_extracurriculares:
            if atividade.nome == nome:
                self.atividades_extracurriculares.remove(atividade)
                messagebox.showinfo("Sucesso", f"Atividade {nome} excluída com sucesso.")
                return
        messagebox.showwarning("Atenção", f"Atividade {nome} não encontrada.")

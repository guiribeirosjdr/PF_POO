import tkinter as tk
from tkinter import ttk, messagebox
from models.curso import Curso  

class GerenciarCursos:
    def __init__(self, master, cursos):
        self.master = master  # Janela principal.
        self.cursos = cursos  # Lista que armazena os cursos existentes.
        self.create_widgets()  # Inicializa os widgets na interface.

    def create_widgets(self):
        self.frame = tk.Frame(self.master)  # Cria um frame para organizar os widgets.
        self.frame.pack(pady=10, padx=10)  # Adiciona padding para melhor estética.

        # Label e Entry para o nome do curso.
        tk.Label(self.frame, text="Nome do Curso:").grid(row=0, column=0, pady=5)
        self.entry_curso = tk.Entry(self.frame)
        self.entry_curso.grid(row=0, column=1, pady=5)

        # Label e Entry para a carga horária do curso.
        tk.Label(self.frame, text="Carga Horária:").grid(row=1, column=0, pady=5)
        self.entry_carga_horaria = tk.Entry(self.frame)
        self.entry_carga_horaria.grid(row=1, column=1, pady=5)

        # Botões para adicionar, remover e listar cursos.
        tk.Button(self.frame, text="Adicionar Curso", command=self.adicionar_curso).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.frame, text="Remover Curso", command=self.remover_curso).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Cursos", command=self.listar_cursos).grid(row=4, columnspan=2, pady=10)

    def adicionar_curso(self):
        curso_nome = self.entry_curso.get()
        carga_horaria = self.entry_carga_horaria.get()

        try:
            carga_horaria = int(carga_horaria)  # Tentativa de conversão para inteiro.
            if carga_horaria > 0:
                novo_curso = Curso(curso_nome, carga_horaria)
                self.cursos.append(novo_curso)
                messagebox.showinfo("Sucesso", "Curso adicionado com sucesso.")
                self.entry_curso.delete(0, tk.END)
                self.entry_carga_horaria.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "A carga horária deve ser um número positivo.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para a carga horária.")

    def remover_curso(self):
        curso_nome = self.entry_curso.get()
        curso_existente = any(curso.nome == curso_nome for curso in self.cursos)
        if curso_existente:
            self.cursos = [curso for curso in self.cursos if curso.nome != curso_nome]
            messagebox.showinfo("Sucesso", "Curso removido com sucesso.")
        else:
            messagebox.showerror("Erro", "Curso não encontrado.")

    def listar_cursos(self):
        if self.cursos:
            cursos_info = "\n".join([f"{curso.nome} - {curso.carga_horaria} horas" for curso in self.cursos])
            messagebox.showinfo("Cursos", cursos_info)
        else:
            messagebox.showinfo("Cursos", "Nenhum curso cadastrado.")

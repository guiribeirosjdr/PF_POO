import tkinter as tk
from tkinter import ttk, messagebox
from models.materia_optativa import MateriaOptativa  

class GerenciarMateriasOptativas:
    def __init__(self, master, materias_optativas, professores, alunos):
        self.master = master  # Janela principal do aplicativo
        self.master.title("Gerenciar Matérias Optativas")  # Define o título da janela
        self.materias_optativas = materias_optativas  # Lista de matérias optativas
        self.professores = professores  # Lista de professores
        self.alunos = alunos  # Lista de alunos

        self.create_widgets()  # Chamada do método para criar os widgets na interface

    def create_widgets(self):
        # Cria um frame na janela principal para organizar os widgets
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)  # Empacota o frame com espaçamento

        # Cria e posiciona um label e um campo de entrada para o nome da matéria optativa
        tk.Label(self.frame, text="Nome:").grid(row=0, column=0, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        # Cria e posiciona um label e um combobox para selecionar o responsável pela matéria optativa
        tk.Label(self.frame, text="Responsável:").grid(row=1, column=0, pady=5)
        self.combo_responsavel = ttk.Combobox(self.frame, values=[p.nome for p in self.professores] + [a.nome for a in self.alunos])
        self.combo_responsavel.grid(row=1, column=1, pady=5)

        # Cria e posiciona um label e um campo de entrada para a carga horária
        tk.Label(self.frame, text="Carga Horária:").grid(row=2, column=0, pady=5)
        self.entry_carga_horaria = tk.Entry(self.frame)
        self.entry_carga_horaria.grid(row=2, column=1, pady=5)

        # Cria e posiciona um label e um listbox para selecionar os participantes
        tk.Label(self.frame, text="Participantes:").grid(row=3, column=0, pady=5)
        self.listbox_participantes = tk.Listbox(self.frame, selectmode=tk.MULTIPLE)
        for aluno in self.alunos:
            self.listbox_participantes.insert(tk.END, aluno.nome)
        self.listbox_participantes.grid(row=3, column=1, pady=5)

        # Cria e posiciona botões para adicionar, listar e excluir matérias optativas
        tk.Button(self.frame, text="Adicionar Matéria Optativa", command=self.adicionar_materia_optativa).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Matérias Optativas", command=self.listar_materias_optativas).grid(row=5, columnspan=2, pady=10)
        tk.Button(self.frame, text="Excluir Matéria Optativa", command=self.excluir_materia_optativa).grid(row=6, columnspan=2, pady=10)

    def adicionar_materia_optativa(self):
        # Adiciona uma matéria optativa à lista após validar a entrada
        nome = self.entry_nome.get()
        responsavel = self.combo_responsavel.get()
        try:
            carga_horaria = int(self.entry_carga_horaria.get())  # Tenta converter a entrada de carga horária para inteiro
        except ValueError:
            messagebox.showerror("Erro", "Carga horária inválida. Por favor, insira um número inteiro.")
            return

        participantes = [self.alunos[i] for i in self.listbox_participantes.curselection()]

        if nome and responsavel and carga_horaria > 0 and participantes:
            materia_optativa = MateriaOptativa(nome, carga_horaria, responsavel, participantes)
            self.materias_optativas.append(materia_optativa)
            messagebox.showinfo("Sucesso", "Matéria Optativa adicionada com sucesso")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente")

    def listar_materias_optativas(self):
        # Lista todas as matérias optativas
        if self.materias_optativas:
            materias_info = "\n".join([materia.exibir_informacoes() for materia in self.materias_optativas])
            messagebox.showinfo("Lista de Matérias Optativas", materias_info)
        else:
            messagebox.showinfo("Lista de Matérias Optativas", "Nenhuma matéria optativa cadastrada.")

    def excluir_materia_optativa(self):
        # Exclui uma matéria optativa com base no nome fornecido
        nome = self.entry_nome.get()
        for materia in self.materias_optativas:
            if materia.nome == nome:
                self.materias_optativas.remove(materia)
                messagebox.showinfo("Sucesso", f"Matéria Optativa {nome} excluída com sucesso.")
                self.limpar_campos()
                return
        messagebox.showwarning("Atenção", f"Matéria Optativa {nome} não encontrada.")

    def limpar_campos(self):
        # Limpa os campos de entrada após a adição ou exclusão
        self.entry_nome.delete(0, tk.END)
        self.combo_responsavel.set('')
        self.entry_carga_horaria.delete(0, tk.END)
        self.listbox_participantes.selection_clear(0, tk.END)


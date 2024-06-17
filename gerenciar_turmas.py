import tkinter as tk
from tkinter import ttk, messagebox
from models.turma import Turma

class GerenciarTurmas:
    def __init__(self, master, turmas, professores, alunos):
        # Inicializa o frame principal do Tkinter
        self.master = master
        self.master.title("Gerenciar Turmas")
        self.turmas = turmas
        self.professores = professores
        self.alunos = alunos

        # Cria os widgets da interface
        self.create_widgets()

    def create_widgets(self):
        # Cria e empacota o frame principal
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)

        # Label e entrada para o nome da turma
        tk.Label(self.frame, text="Nome:").grid(row=0, column=0, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        # Label e entrada para o curso da turma
        tk.Label(self.frame, text="Curso:").grid(row=1, column=0, pady=5)
        self.entry_curso = tk.Entry(self.frame)
        self.entry_curso.grid(row=1, column=1, pady=5)

        # Label e combobox para selecionar o professor da turma
        tk.Label(self.frame, text="Professor:").grid(row=2, column=0, pady=5)
        self.combo_professor = ttk.Combobox(self.frame, values=[professor.nome for professor in self.professores])
        self.combo_professor.grid(row=2, column=1, pady=5)

        # Label e listbox para selecionar os alunos da turma
        tk.Label(self.frame, text="Alunos:").grid(row=3, column=0, pady=5)
        self.listbox_alunos = tk.Listbox(self.frame, selectmode=tk.MULTIPLE)
        for aluno in self.alunos:
            self.listbox_alunos.insert(tk.END, aluno.nome)
        self.listbox_alunos.grid(row=3, column=1, pady=5)

        # Botões para adicionar, excluir turma, lançar nota e presença
        tk.Button(self.frame, text="Adicionar Turma", command=self.adicionar_turma).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.frame, text="Excluir Turma", command=self.excluir_turma).grid(row=6, columnspan=2, pady=10)
        tk.Button(self.frame, text="Lançar Nota", command=self.lancar_nota).grid(row=7, columnspan=2, pady=10)
        tk.Button(self.frame, text="Lançar Presença", command=self.lancar_presenca).grid(row=8, columnspan=2, pady=10)

    def adicionar_turma(self):
        # Obtém os dados da turma dos campos de entrada
        nome = self.entry_nome.get()
        curso_nome = self.entry_curso.get()
        professor = next((professor for professor in self.professores if professor.nome == self.combo_professor.get()), None)
        alunos = [self.alunos[i] for i in self.listbox_alunos.curselection()]

        # Verifica se todos os campos foram preenchidos
        if not (nome and curso_nome and professor and alunos):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        # Cria e adiciona a nova turma à lista de turmas
        turma = Turma(nome, curso_nome, professor, alunos)
        self.turmas.append(turma)

        # Mostra mensagem de sucesso e limpa os campos
        messagebox.showinfo("Sucesso", "Turma adicionada com sucesso")
        self.limpar_campos()

    def excluir_turma(self):
        # Obtém o nome da turma a ser excluída
        nome = self.entry_nome.get()
        turma = next((turma for turma in self.turmas if turma.nome == nome), None)
        if turma:
            self.turmas.remove(turma)
            messagebox.showinfo("Sucesso", "Turma excluída com sucesso")
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", "Turma não encontrada")

    def lancar_nota(self):
        # Cria uma nova janela para lançar notas
        self.janela_lancar_nota = tk.Toplevel(self.master)
        self.janela_lancar_nota.title("Lançar Nota")

        # Label e combobox para selecionar a turma
        tk.Label(self.janela_lancar_nota, text="Selecione a Turma:").pack(pady=5)
        self.combo_turma = ttk.Combobox(self.janela_lancar_nota, values=[turma.nome for turma in self.turmas])
        self.combo_turma.pack(pady=5)

        # Label e combobox para selecionar o aluno
        tk.Label(self.janela_lancar_nota, text="Selecione o Aluno:").pack(pady=5)
        self.combo_aluno = ttk.Combobox(self.janela_lancar_nota, values=[aluno.nome for aluno in self.alunos])
        self.combo_aluno.pack(pady=5)

        # Label e entrada para a nota
        tk.Label(self.janela_lancar_nota, text="Nota:").pack(pady=5)
        self.entry_nota = tk.Entry(self.janela_lancar_nota)
        self.entry_nota.pack(pady=5)

        # Botão para salvar a nota
        tk.Button(self.janela_lancar_nota, text="Lançar", command=self.salvar_nota).pack(pady=10)

    def salvar_nota(self):
        # Obtém os dados da nota dos campos de entrada
        nome_turma = self.combo_turma.get()
        nome_aluno = self.combo_aluno.get()
        try:
            nota = float(self.entry_nota.get())
        except ValueError:
            messagebox.showerror("Erro", "Nota inválida. Por favor, insira um número válido.")
            return

        # Encontra a turma e o aluno correspondentes
        turma = next((turma for turma in self.turmas if turma.nome == nome_turma), None)
        aluno = next((aluno for aluno in turma.alunos if aluno.nome == nome_aluno), None)

        # Lança a nota para o aluno na turma
        if turma and aluno:
            turma.lancar_nota(aluno, nota)
            messagebox.showinfo("Sucesso", "Nota lançada com sucesso")
            self.janela_lancar_nota.destroy()
        else:
            messagebox.showerror("Erro", "Turma ou aluno não encontrado.")

    def lancar_presenca(self):
        # Cria uma nova janela para lançar presenças
        self.janela_lancar_presenca = tk.Toplevel(self.master)
        self.janela_lancar_presenca.title("Lançar Presença")

        # Label e combobox para selecionar a turma
        tk.Label(self.janela_lancar_presenca, text="Selecione a Turma:").pack(pady=5)
        self.combo_turma_presenca = ttk.Combobox(self.janela_lancar_presenca, values=[turma.nome for turma in self.turmas])
        self.combo_turma_presenca.pack(pady=5)

        # Label e combobox para selecionar o aluno
        tk.Label(self.janela_lancar_presenca, text="Selecione o Aluno:").pack(pady=5)
        self.combo_aluno_presenca = ttk.Combobox(self.janela_lancar_presenca, values=[aluno.nome for aluno in self.alunos])
        self.combo_aluno_presenca.pack(pady=5)

        # Label e combobox para selecionar a presença (Sim/Não)
        tk.Label(self.janela_lancar_presenca, text="Presença (Sim/Não):").pack(pady=5)
        self.combo_presenca = ttk.Combobox(self.janela_lancar_presenca, values=["Sim", "Não"])
        self.combo_presenca.pack(pady=5)

        # Botão para salvar a presença
        tk.Button(self.janela_lancar_presenca, text="Lançar", command=self.salvar_presenca).pack(pady=10)

    def salvar_presenca(self):
        # Obtém os dados da presença dos campos de entrada
        nome_turma = self.combo_turma_presenca.get()
        nome_aluno = self.combo_aluno_presenca.get()
        presenca = self.combo_presenca.get()

        # Encontra a turma e o aluno correspondentes
        turma = next((turma for turma in self.turmas if turma.nome == nome_turma), None)
        aluno = next((aluno for aluno in turma.alunos if aluno.nome == nome_aluno), None)

        # Lança a presença para o aluno na turma
        if turma and aluno:
            turma.lancar_presenca(aluno, presenca == "Sim")
            messagebox.showinfo("Sucesso", "Presença lançada com sucesso")
            self.janela_lancar_presenca.destroy()
        else:
            messagebox.showerror("Erro", "Turma ou aluno não encontrado.")

    def limpar_campos(self):
        # Limpa os campos de entrada do formulário
        self.entry_nome.delete(0, tk.END)
        self.entry_curso.delete(0, tk.END)
        self.combo_professor.set('')
        self.listbox_alunos.selection_clear(0, tk.END)

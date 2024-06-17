import tkinter as tk
from tkinter import ttk, messagebox
from models.funcionario import Funcionario  

class GerenciarFuncionarios:
    def __init__(self, master, funcionarios):
        self.master = master  # Janela principal da aplicação.
        self.funcionarios = funcionarios  # Lista para armazenar os funcionários.
        self.master.title("Gerenciar Funcionários")  # Título da janela.

        self.create_widgets()  # Método para criar e configurar os widgets.

    def create_widgets(self):
        # Configuração dos componentes na janela.
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)  # Empacotamento com padding para estética.

        # Campos de entrada para nome, cargo, horário e email.
        tk.Label(self.frame, text="Nome:").grid(row=0, column=0, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="Cargo:").grid(row=1, column=0, pady=5)
        self.entry_cargo = tk.Entry(self.frame)
        self.entry_cargo.grid(row=1, column=1, pady=5)

        tk.Label(self.frame, text="Horário:").grid(row=2, column=0, pady=5)
        self.entry_horario = tk.Entry(self.frame)
        self.entry_horario.grid(row=2, column=1, pady=5)

        tk.Label(self.frame, text="Email:").grid(row=3, column=0, pady=5)
        self.entry_email = tk.Entry(self.frame)
        self.entry_email.grid(row=3, column=1, pady=5)

        # Botões para adicionar, listar e excluir funcionários.
        tk.Button(self.frame, text="Adicionar Funcionário", command=self.adicionar_funcionario).grid(row=4, columnspan=2, pady=10)
        tk.Button(self.frame, text="Listar Funcionários", command=self.listar_funcionarios).grid(row=5, columnspan=2, pady=10)
        tk.Button(self.frame, text="Excluir Funcionário", command=self.excluir_funcionario).grid(row=6, columnspan=2, pady=10)

    def adicionar_funcionario(self):
        # Coleta dados dos campos de entrada e adiciona um novo funcionário à lista.
        nome = self.entry_nome.get()
        cargo = self.entry_cargo.get()
        horario = self.entry_horario.get()
        email = self.entry_email.get()

        funcionario = Funcionario(nome, cargo, horario, email)
        self.funcionarios.append(funcionario)

        messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso")
        # Limpar campos após adição
        self.entry_nome.delete(0, tk.END)
        self.entry_cargo.delete(0, tk.END)
        self.entry_horario.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)

    def listar_funcionarios(self):
        # Gera uma lista formatada dos funcionários para exibição.
        funcionarios_info = "\n".join([funcionario.exibir_informacoes() for funcionario in self.funcionarios])
        messagebox.showinfo("Lista de Funcionários", funcionarios_info)

    def excluir_funcionario(self):
        # Exclui um funcionário baseado no nome fornecido.
        nome = self.entry_nome.get()
        inicial_count = len(self.funcionarios)
        self.funcionarios = [func for func in self.funcionarios if func.nome != nome]
        if len(self.funcionarios) < inicial_count:
            messagebox.showinfo("Sucesso", f"Funcionário {nome} excluído com sucesso.")
        else:
            messagebox.showwarning("Atenção", f"Funcionário {nome} não encontrado.")

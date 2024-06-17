import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class GerenciarSeguranca:
    def __init__(self, master, seguranca, funcionarios):
        self.master = master
        self.seguranca = seguranca
        self.funcionarios = funcionarios

        # Configuração da interface
        tk.Label(master, text="Funcionário para Ronda").grid(row=0, column=0)
        self.combo_funcionarios = ttk.Combobox(master, values=[funcionario.nome for funcionario in self.funcionarios])
        self.combo_funcionarios.grid(row=0, column=1)

        tk.Button(master, text="Iniciar Ronda", command=self.iniciar_ronda).grid(row=1, column=0, columnspan=2)

        # Telefones úteis
        tk.Label(master, text="Telefones Úteis").grid(row=2, column=0, columnspan=2)
        ttk.Label(master, text="Polícia: 190").grid(row=3, column=0, columnspan=2)
        ttk.Label(master, text="Bombeiros: 193").grid(row=4, column=0, columnspan=2)
        ttk.Label(master, text="SAMU: 192").grid(row=5, column=0, columnspan=2)

    def iniciar_ronda(self):
        # Validação de entrada
        funcionario_nome = self.combo_funcionarios.get()
        if not funcionario_nome:
            messagebox.showerror("Erro", "Por favor, selecione um funcionário.")
            return

        # Procura o funcionário na lista
        funcionario = next((f for f in self.funcionarios if f.nome == funcionario_nome), None)
        if funcionario:
            mensagem = self.seguranca.iniciar_ronda(funcionario)
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showerror("Erro", "Funcionário não encontrado.")

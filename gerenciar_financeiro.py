import tkinter as tk
from tkinter import messagebox

class GerenciarFinanceiro:
    def __init__(self, master, financeiro):
        self.master = master  # Janela principal da aplicação.
        self.financeiro = financeiro  # Objeto de controle financeiro.

        # Configuração dos labels e entries para nome e valor das transações.
        tk.Label(master, text="Nome").grid(row=0)
        tk.Label(master, text="Valor").grid(row=1)

        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1)
        self.entry_valor = tk.Entry(master)
        self.entry_valor.grid(row=1, column=1)

        # Botões para adicionar receita, despesa e listar informações financeiras.
        tk.Button(master, text="Adicionar Receita", command=self.adicionar_receita).grid(row=2, column=0)
        tk.Button(master, text="Adicionar Despesa", command=self.adicionar_despesa).grid(row=2, column=1)
        tk.Button(master, text="Listar Informações", command=self.listar_informacoes).grid(row=3, column=0, columnspan=2)

    def adicionar_receita(self):
        # Adiciona uma receita ao registro financeiro após validação.
        nome = self.entry_nome.get()
        try:
            valor = float(self.entry_valor.get())
            self.financeiro.registrar_pagamento(nome, valor)
            messagebox.showinfo("Sucesso", "Receita adicionada com sucesso.")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Por favor, insira um número.")

    def adicionar_despesa(self):
        # Adiciona uma despesa ao registro financeiro após validação.
        nome = self.entry_nome.get()
        try:
            valor = float(self.entry_valor.get())
            self.financeiro.registrar_despesa(nome, valor)
            messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso.")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido. Por favor, insira um número.")

    def listar_informacoes(self):
        # Mostra um resumo das informações financeiras.
        info = self.financeiro.exibir_informacoes()
        messagebox.showinfo("Informações Financeiras", info)

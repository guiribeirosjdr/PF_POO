import tkinter as tk
from tkinter import messagebox
from models.campeonato import Campeonato  

class GerenciarCampeonatos:
    def __init__(self, master, campeonatos, turmas):
        self.master = master  # Janela principal da aplicação.
        self.campeonatos = campeonatos  # Lista de campeonatos gerenciados.
        self.turmas = turmas  # Lista de turmas disponíveis para participação nos campeonatos.
        master.title("Gerenciar Campeonatos")  # Define o título da janela.

        self.create_widgets()  # Método para criar widgets.

    def create_widgets(self):
        # Cria e organiza os widgets na janela.
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10)  # Empacotamento com padding.

        # Campo de entrada para o nome do campeonato.
        tk.Label(self.frame, text="Nome do Campeonato:").grid(row=0, column=0, pady=5)
        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, pady=5)

        # Listbox para selecionar múltiplas turmas participantes.
        tk.Label(self.frame, text="Turmas Participantes:").grid(row=1, column=0, pady=5)
        self.listbox_turmas = tk.Listbox(self.frame, selectmode=tk.MULTIPLE)
        for turma in self.turmas:
            self.listbox_turmas.insert(tk.END, turma.nome)
        self.listbox_turmas.grid(row=1, column=1, pady=5)

        # Botões para adicionar e excluir campeonatos.
        tk.Button(self.frame, text="Adicionar Campeonato", command=self.adicionar_campeonato).grid(row=2, columnspan=2, pady=10)
        tk.Button(self.frame, text="Excluir Campeonato", command=self.excluir_campeonato).grid(row=4, columnspan=2, pady=10)

    def adicionar_campeonato(self):
        # Coleta os dados, cria um novo campeonato e o adiciona à lista.
        nome = self.entry_nome.get()
        turmas = [self.turmas[i] for i in self.listbox_turmas.curselection()]

        if nome and turmas:
            campeonato = Campeonato(nome)
            for turma in turmas:
                campeonato.adicionar_turma(turma)
            self.campeonatos.append(campeonato)
            messagebox.showinfo("Sucesso", "Campeonato adicionado com sucesso")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos")

    def excluir_campeonato(self):
        # Exclui um campeonato com base no nome fornecido.
        nome = self.entry_nome.get()
        for campeonato in self.campeonatos:
            if campeonato.nome == nome:
                self.campeonatos.remove(campeonato)
                messagebox.showinfo("Sucesso", f"Campeonato {nome} excluído com sucesso.")
                return
        messagebox.showwarning("Atenção", f"Campeonato {nome} não encontrado.")

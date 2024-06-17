import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from models.sala import Sala, Reserva  

class GerenciarReservas:
    def __init__(self, master, salas, turmas):
        self.master = master  # Janela principal do aplicativo
        self.salas = salas  # Lista de salas disponíveis
        self.turmas = turmas  # Lista de turmas disponíveis
        master.title("Gerenciar Reservas")  # Define o título da janela

        self.frame = tk.Frame(master)
        self.frame.pack(pady=10, padx=10)  # Empacota o frame com espaçamento

        self.create_widgets()  # Chamada do método para criar os widgets na interface

        # Campos para entrada de data e hora de início e fim da reserva
        self.label_inicio = tk.Label(master, text="Início (YYYY-MM-DD HH:MM)")
        self.label_inicio.pack()
        self.entry_inicio = tk.Entry(master)
        self.entry_inicio.pack()

        self.label_fim = tk.Label(master, text="Fim (YYYY-MM-DD HH:MM)")
        self.label_fim.pack()
        self.entry_fim = tk.Entry(master)
        self.entry_fim.pack()

        # Botões para reservar, verificar disponibilidade e listar reservas
        self.button_reservar = tk.Button(master, text="Reservar Sala", command=self.reservar_sala)
        self.button_reservar.pack()

        self.button_verificar = tk.Button(master, text="Verificar Disponibilidade", command=self.verificar_disponibilidade)
        self.button_verificar.pack()

        self.button_listar_reservas = tk.Button(master, text="Listar Reservas", command=self.listar_reservas)
        self.button_listar_reservas.pack()

    def create_widgets(self):
        # Criação e posicionamento de widgets para seleção de sala e turma
        tk.Label(self.frame, text="Escolha a Sala:").grid(row=0, column=0, pady=5)
        self.combo_sala = ttk.Combobox(self.frame, values=[sala.numero for sala in self.salas])
        self.combo_sala.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="Escolha a Turma:").grid(row=1, column=0, pady=5)
        self.combo_turma = ttk.Combobox(self.frame, values=[turma.nome for turma in self.turmas])
        self.combo_turma.grid(row=1, column=1, pady=5)

    def reservar_sala(self):
        # Realiza a reserva de uma sala após validar as entradas
        numero_sala = self.combo_sala.get()
        nome_turma = self.combo_turma.get()
        inicio = self.entry_inicio.get()
        fim = self.entry_fim.get()

        sala = next((s for s in self.salas if s.numero == numero_sala), None)
        turma = next((t for t in self.turmas if t.nome == nome_turma), None)

        if sala and turma:
            try:
                inicio_dt = datetime.strptime(inicio, "%Y-%m-%d %H:%M")
                fim_dt = datetime.strptime(fim, "%Y-%m-%d %H:%M")
                if sala.reservar(turma, inicio_dt, fim_dt):
                    messagebox.showinfo("Sucesso", "Sala reservada com sucesso")
                else:
                    messagebox.showerror("Erro", "Sala não está disponível no período solicitado")
            except ValueError:
                messagebox.showerror("Erro", "Formato de data/hora inválido")
        else:
            messagebox.showerror("Erro", "Sala ou Turma não encontrada")

    def verificar_disponibilidade(self):
        # Verifica a disponibilidade de uma sala para o período informado
        numero_sala = self.combo_sala.get()
        inicio = self.entry_inicio.get()
        fim = self.entry_fim.get()

        sala = next((s for s in self.salas if s.numero == numero_sala), None)

        if sala:
            try:
                inicio_dt = datetime.strptime(inicio, "%Y-%m-%d %H:%M")
                fim_dt = datetime.strptime(fim, "%Y-%m-%d %H:%M")
                if sala.verificar_disponibilidade(inicio_dt, fim_dt):
                    messagebox.showinfo("Disponível", "Sala está disponível no período solicitado")
                else:
                    messagebox.showerror("Indisponível", "Sala não está disponível no período solicitado")
            except ValueError:
                messagebox.showerror("Erro", "Formato de data/hora inválido")
        else:
            messagebox.showerror("Erro", "Sala não encontrada")

    def listar_reservas(self):
        # Lista as reservas para uma sala específica
        numero_sala = self.combo_sala.get()
        sala = next((s for s in self.salas if s.numero == numero_sala), None)

        if sala:
            reservas_info = sala.exibir_informacoes()
            messagebox.showinfo("Reservas", reservas_info)
        else:
            messagebox.showerror("Erro", "Sala não encontrada")

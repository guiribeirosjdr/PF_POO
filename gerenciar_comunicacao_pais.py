import tkinter as tk
from tkinter import ttk, messagebox
from models.comunicacao_pais import ComunicacaoPais

class GerenciarComunicacaoPais:
    def __init__(self, master, comunicacao_pais, turmas, alunos, professores, funcionarios):
        # Inicializa o frame principal do Tkinter
        self.master = master
        # Instância da classe de comunicação com pais
        self.comunicacao_pais = comunicacao_pais
        # Listas de turmas, alunos, professores e funcionários
        self.turmas = turmas
        self.alunos = alunos
        self.professores = professores
        self.funcionarios = funcionarios
        # Define o título da janela
        master.title("Gerenciar Comunicação")

        # Cria e empacota o label para o destinatário
        self.label_destinatario = tk.Label(master, text="Destinatário")
        self.label_destinatario.pack()

        # Cria e empacota o combobox para selecionar o tipo de destinatário
        self.combo_tipo_destinatario = ttk.Combobox(master, values=["Aluno", "Professor", "Funcionário", "Turma"])
        self.combo_tipo_destinatario.pack()
        # Vincula a seleção do combobox ao método atualizar_destinatarios
        self.combo_tipo_destinatario.bind("<<ComboboxSelected>>", self.atualizar_destinatarios)

        # Cria e empacota o label para escolher o destino
        self.label_destino = tk.Label(master, text="Escolha o Destino")
        self.label_destino.pack()

        # Cria e empacota o combobox para selecionar o destino específico
        self.combo_destino = ttk.Combobox(master)
        self.combo_destino.pack()

        # Cria e empacota o label para a mensagem
        self.label_mensagem = tk.Label(master, text="Mensagem")
        self.label_mensagem.pack()
        # Cria e empacota o campo de entrada para a mensagem
        self.entry_mensagem = tk.Entry(master)
        self.entry_mensagem.pack()

        # Cria e empacota o botão para enviar a mensagem
        self.button_enviar = tk.Button(master, text="Enviar Mensagem", command=self.enviar_mensagem)
        self.button_enviar.pack()

    def atualizar_destinatarios(self, event):
        # Obtém o tipo de destinatário selecionado
        tipo_destinatario = self.combo_tipo_destinatario.get()
        # Atualiza o combobox de destino com base no tipo de destinatário selecionado
        if tipo_destinatario == "Aluno":
            self.combo_destino['values'] = [aluno.nome for aluno in self.alunos]
        elif tipo_destinatario == "Professor":
            self.combo_destino['values'] = [professor.nome for professor in self.professores]
        elif tipo_destinatario == "Funcionário":
            self.combo_destino['values'] = [funcionario.nome for funcionario in self.funcionarios]
        elif tipo_destinatario == "Turma":
            self.combo_destino['values'] = [turma.identificador for turma in self.turmas]

    def enviar_mensagem(self):
        # Obtém o tipo de destinatário, destino específico e mensagem
        tipo_destinatario = self.combo_tipo_destinatario.get()
        destino = self.combo_destino.get()
        mensagem = self.entry_mensagem.get()

        # Encontra o destinatário correspondente com base no tipo de destinatário
        if tipo_destinatario == "Aluno":
            destinatario = next((a for a in self.alunos if a.nome == destino), None)
        elif tipo_destinatario == "Professor":
            destinatario = next((p for p in self.professores if p.nome == destino), None)
        elif tipo_destinatario == "Funcionário":
            destinatario = next((f for f in self.funcionarios if f.nome == destino), None)
        elif tipo_destinatario == "Turma":
            turma = next((t for t in self.turmas if t.identificador == destino), None)
            destinatario = turma.alunos if turma else []

        # Envia a mensagem para o destinatário ou turma selecionada
        if destinatario:
            if isinstance(destinatario, list):  # Se o destinatário é uma lista (Turma)
                for aluno in destinatario:
                    self.comunicacao_pais.enviar_mensagem(aluno.email, mensagem)
                messagebox.showinfo("Sucesso", "Mensagem enviada para todos os alunos da turma")
            else:
                self.comunicacao_pais.enviar_mensagem(destinatario.email, mensagem)
                messagebox.showinfo("Sucesso", f"Mensagem enviada para {destino}")
        else:
            messagebox.showerror("Erro", "Destinatário não encontrado")

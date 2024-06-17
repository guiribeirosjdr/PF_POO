# Importa a biblioteca tkinter para a criação da interface gráfica e ttk para componentes estilizados.
import tkinter as tk
from tkinter import ttk

# Importa as classes de interface para cada parte do sistema de gestão.
from gui.gerenciar_alunos import GerenciarAlunos
from gui.gerenciar_professores import GerenciarProfessores
from gui.gerenciar_turmas import GerenciarTurmas
from gui.gerenciar_salas import GerenciarSalas
from gui.gerenciar_materias_optativas import GerenciarMateriasOptativas
from gui.gerenciar_atividades_extracurriculares import GerenciarAtividadesExtracurriculares
from gui.gerenciar_campeonatos import GerenciarCampeonatos
from gui.gerenciar_reservas import GerenciarReservas
from gui.gerenciar_financeiro import GerenciarFinanceiro
from gui.gerenciar_comunicacao_pais import GerenciarComunicacaoPais
from gui.gerenciar_biblioteca import GerenciarBiblioteca
from gui.gerenciar_seguranca import GerenciarSeguranca
from gui.gerenciar_funcionarios import GerenciarFuncionarios
from gui.gerenciar_inventario import GerenciarInventario
from gui.gestao_eventos import GestaoEventos
from gui.gerenciar_cursos import GerenciarCursos

# Importa classes do modelo que representam diferentes partes do sistema escolar.
from models.financeiro import Financeiro
from models.comunicacao_pais import ComunicacaoPais
from models.biblioteca import Biblioteca
from models.seguranca import Seguranca
from models.inventario import Inventario
from models.evento import Evento
from models.persistence import salvar_dados, carregar_dados

class SistemaGestaoEscolar:
    def __init__(self, master, alunos, professores, turmas, salas, cursos,
                 materias_optativas, atividades_extracurriculares, campeonatos,
                 financeiro, comunicacao_pais, biblioteca, avaliacoes,
                 seguranca, relatorios, funcionarios, inventario, eventos):
        self.master = master # Janela principal
        master.title("Sistema de Gestão Escolar") # Título da janela principal

 # Inicializa as variáveis de instância com os dados passados para o construtor.
        self.dados_arquivo = "dados_sistema.pkl"
        
        self.alunos = alunos
        self.professores = professores
        self.turmas = turmas
        self.salas = salas
        self.cursos = cursos
        self.materias_optativas = materias_optativas
        self.atividades_extracurriculares = atividades_extracurriculares
        self.campeonatos = campeonatos
        self.financeiro = financeiro
        self.comunicacao_pais = comunicacao_pais
        self.biblioteca = biblioteca
        self.avaliacoes = avaliacoes
        self.seguranca = seguranca
        self.relatorios = relatorios
        self.funcionarios = funcionarios
        self.inventario = inventario
        self.eventos = eventos

        self.notebook = ttk.Notebook(master) # Cria um widget de notebook (abas) na janela principal.
        self.notebook.pack(expand=1, fill='both') # Expande e preenche o espaço disponível.

 # Métodos para criar abas específicas e suas funcionalidades.
 
        # Bem-vindo
        self.frame_bem_vindo = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_bem_vindo, text="Bem-vindo")
        self.create_bem_vindo(self.frame_bem_vindo)

        # Gestão de Pessoas
        self.frame_pessoas = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_pessoas, text="Gestão de Pessoas")
        self.create_gestao_pessoas(self.frame_pessoas)

        # Gestão Administrativa
        self.frame_administrativa = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_administrativa, text="Gestão Administrativa")
        self.create_gestao_administrativa(self.frame_administrativa)

        # Gestão Financeira
        self.frame_financeira = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_financeira, text="Gestão Financeira")
        self.create_gestao_financeira(self.frame_financeira)

        # Gestão Pedagógica
        self.frame_pedagogica = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_pedagogica, text="Gestão Pedagógica")
        self.create_gestao_pedagogica(self.frame_pedagogica)

        # Gestão de Comunicação
        self.frame_comunicacao = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_comunicacao, text="Gestão de Comunicação")
        self.create_gestao_comunicacao(self.frame_comunicacao)

        # Gestão do Cotidiano Escolar
        self.frame_cotidiano = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_cotidiano, text="Gestão do Cotidiano Escolar")
        self.create_gestao_cotidiano(self.frame_cotidiano)
        
        # Gestão de Segurança
        self.frame_seguranca = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_seguranca, text="Segurança")
        self.create_gestao_seguranca(self.frame_seguranca)
        
        # Gestão de Reservas
        self.frame_reservas = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_reservas, text="Gestão de Reservas")
        self.create_gestao_reservas(self.frame_reservas)

        # Gestão de Cursos
        self.frame_cursos = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_cursos, text="Gestão de Cursos")
        self.create_gestao_cursos(self.frame_cursos)

# Método para salvar os dados atuais do sistema antes de fechar a aplicação.
        self.master.protocol("WM_DELETE_WINDOW", self.salvar_dados)

    def salvar_dados(self):
        dados = [self.alunos, self.professores, self.turmas, self.salas, self.cursos,
                 self.materias_optativas, self.atividades_extracurriculares, self.campeonatos,
                 self.financeiro, self.comunicacao_pais, self.biblioteca, self.avaliacoes,
                 self.seguranca, self.relatorios, self.funcionarios, self.inventario, self.eventos]
        salvar_dados(self.dados_arquivo, dados)
        self.master.destroy()

 # Métodos create para inicializar os widgets nas diferentes abas
    def create_bem_vindo(self, parent):
        tk.Label(parent, text="Bem-vindo ao Sistema de Gestão Escolar \nEste sistema foi desenvolvido para gerenciar diversas áreas de uma instituição escolar.", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(parent, text="Trata-se de um projeto final da disciplina de Programação Orientada a Objetos.", wraplength=500).pack(pady=10)
        tk.Label(parent, text="Desenvolvido por Guilherme Augusto e Arthur Rangel \nTodos os direitos reservados.", wraplength=500).pack(pady=10)

    def create_gestao_pessoas(self, parent):
        tk.Button(parent, text="Cadastrar Alunos", command=self.gerenciar_alunos).pack()
        tk.Button(parent, text="Gerenciar Professores", command=self.gerenciar_professores).pack()
        tk.Button(parent, text="Gerenciar Funcionários", command=self.gerenciar_funcionarios).pack()

    def create_gestao_administrativa(self, parent):
        tk.Button(parent, text="Gerenciar Salas", command=self.gerenciar_salas).pack()
        tk.Button(parent, text="Gestão de Ativos e Inventário", command=self.gerenciar_inventario).pack()
        
    def create_gestao_cursos(self, parent):
        frame = tk.Frame(parent)
        frame.pack(pady=10, padx=10)
        tk.Button(frame, text="Gerenciar Cursos", command=self.gerenciar_cursos).grid(row=0, column=0, padx=10, pady=10)

    def create_gestao_pedagogica(self, parent):
        tk.Button(parent, text="Gerenciar Turmas", command=self.gerenciar_turmas).pack()
        tk.Button(parent, text="Gerenciar Matérias Optativas", command=self.gerenciar_materias_optativas).pack()
        tk.Button(parent, text="Biblioteca", command=self.gerenciar_biblioteca).pack()
        
    def create_gestao_reservas(self, parent):
        frame = tk.Frame(parent)
        frame.pack(pady=10, padx=10)
        tk.Button(frame, text="Gerenciar Reservas de Salas", command=self.gerenciar_reservas).grid(row=0, column=0, padx=10, pady=10)

    def create_gestao_comunicacao(self, parent):
        tk.Button(parent, text="Comunicação", command=self.gerenciar_comunicacao_pais).pack()

    def create_gestao_cotidiano(self, parent):
        tk.Button(parent, text="Gerenciar Atividades Extracurriculares", command=self.gerenciar_atividades_extracurriculares).pack()
        tk.Button(parent, text="Gerenciar Campeonatos", command=self.gerenciar_campeonatos).pack()
        tk.Button(parent, text="Agenda e Gestão de Eventos", command=self.gestao_eventos).pack()
        
    def create_gestao_financeira(self, parent):
        tk.Button(parent, text="Gestão Financeira", command=self.gerenciar_financeiro).pack()

    def create_gestao_seguranca(self, tab):
        frame = tk.Frame(tab)
        frame.pack(pady=10, padx=10)
        tk.Button(frame, text="Gerenciar Segurança", command=self.gerenciar_seguranca).grid(row=0, column=0, padx=10, pady=10)
        
# Métodos gerenciar para abrir janelas de gestão específicas.
    def gerenciar_alunos(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarAlunos(self.nova_janela, self.alunos)

    def gerenciar_professores(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarProfessores(self.nova_janela, self.professores)

    def gerenciar_turmas(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarTurmas(self.nova_janela, self.turmas, self.professores, self.alunos)

    def gerenciar_salas(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarSalas(self.nova_janela, self.salas)

    def gerenciar_materias_optativas(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarMateriasOptativas(self.nova_janela, self.materias_optativas, self.professores, self.alunos)

    def gerenciar_atividades_extracurriculares(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarAtividadesExtracurriculares(self.nova_janela, self.atividades_extracurriculares, self.alunos)

    def gerenciar_campeonatos(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarCampeonatos(self.nova_janela, self.campeonatos, self.turmas)

    def gerenciar_reservas(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarReservas(self.nova_janela, self.salas, self.turmas)

    def gerenciar_financeiro(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarFinanceiro(self.nova_janela, self.financeiro)

    def gerenciar_comunicacao_pais(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarComunicacaoPais(self.nova_janela, self.comunicacao_pais, self.turmas, self.alunos, self.professores, self.funcionarios)

    def gerenciar_biblioteca(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarBiblioteca(self.nova_janela, self.biblioteca, self.alunos)

    def gerenciar_seguranca(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarSeguranca(self.nova_janela, self.seguranca, self.funcionarios)

    def gerenciar_funcionarios(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarFuncionarios(self.nova_janela, self.funcionarios)

    def gerenciar_inventario(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarInventario(self.nova_janela, self.inventario)

    def gestao_eventos(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GestaoEventos(self.nova_janela, self.eventos)
        
    def gerenciar_cursos(self):
        self.nova_janela = tk.Toplevel(self.master)
        self.app = GerenciarCursos(self.nova_janela, self.cursos)

if __name__ == "__main__":
    root = tk.Tk() # Cria a janela principal.
    dados = carregar_dados("dados_sistema.pkl") # Tenta carregar dados salvos.
    if not dados:
        dados = ([], [], [], [], [], [], [], [], Financeiro(), ComunicacaoPais(), Biblioteca(), [], Seguranca(), [], [], Inventario(), Evento())
    app = SistemaGestaoEscolar(root, *dados) # Cria uma instância do sistema de gestão.
    root.mainloop() # Inicia o loop principal da interface gráfica.
    # Salva os dados do sistema ao fechar a aplicação.
    salvar_dados("dados_sistema.pkl", (app.alunos, app.professores, app.turmas, app.salas, app.cursos,
                                       app.materias_optativas, app.atividades_extracurriculares, app.campeonatos,
                                       app.financeiro, app.comunicacao_pais, app.biblioteca, app.avaliacoes,
                                       app.seguranca, app.relatorios, app.funcionarios, app.inventario, app.eventos))
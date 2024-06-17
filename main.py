# Importação da biblioteca tkinter para criação de interfaces gráficas.
import tkinter as tk

# Importação de funções para carregar e salvar dados.
from models.persistence import carregar_dados, salvar_dados

# Importação da classe principal da interface gráfica do sistema de gestão escolar.
from gui.main_window import SistemaGestaoEscolar

# Importações de várias classes que representam diferentes módulos do sistema escolar.
from models.financeiro import Financeiro
from models.comunicacao_pais import ComunicacaoPais
from models.biblioteca import Biblioteca
from models.seguranca import Seguranca
from models.inventario import Inventario
from models.evento import Evento

# Verificação para executar o código apenas se o arquivo for o script principal.
if __name__ == "__main__":
    # Inicialização da janela principal do Tkinter.
    root = tk.Tk()

    # Carregamento dos dados do sistema a partir de um arquivo pickle.
    dados = carregar_dados("dados_sistema.pkl")

    # Se nenhum dado for encontrado, inicializa todas as listas e objetos necessários com valores padrão.
    if not dados:
        dados = ([], [], [], [], [], [], [], [], Financeiro(), ComunicacaoPais(), Biblioteca(), [], Seguranca(), [], [], Inventario(), Evento())

    # Criação da aplicação principal, passando a janela e os dados carregados ou criados.
    app = SistemaGestaoEscolar(root, *dados)

    # Início do loop principal da interface gráfica. Este loop mantém a janela aberta.
    root.mainloop()

    # Após o fechamento da janela, os dados são salvos de volta para o arquivo, capturando qualquer estado atualizado da aplicação.
    salvar_dados("dados_sistema.pkl", (app.alunos, app.professores, app.turmas, app.salas, app.cursos,
                                       app.materias_optativas, app.atividades_extracurriculares, app.campeonatos,
                                       app.financeiro, app.comunicacao_pais, app.biblioteca, app.avaliacoes,
                                       app.seguranca, app.relatorios, app.funcionarios, app.inventario, app.eventos))

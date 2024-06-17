class AtividadeExtracurricular:
    def __init__(self, nome, alunos_participantes):
        # Inicialização do objeto com o nome da atividade e a lista de alunos participantes.
        self.nome = nome  # Nome da atividade extracurricular.
        self.alunos_participantes = alunos_participantes  # Lista de objetos aluno que participam da atividade.

    def exibir_informacoes(self):
        # Cria uma lista formatada dos nomes dos alunos participantes com suas matrículas.
        alunos_nomes = [f"{aluno.nome} ({aluno.matricula})" for aluno in self.alunos_participantes]
        # Retorna uma string com o nome da atividade e os participantes formatados.
        return f"Atividade: {self.nome}, Participantes: {', '.join(alunos_nomes)}"

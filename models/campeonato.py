class Campeonato:
    def __init__(self, nome):
        self.nome = nome  # Nome do campeonato.
        self.turmas_participantes = []  # Lista para armazenar as turmas que participam do campeonato.

    def adicionar_turma(self, turma):
        # Adiciona uma turma à lista de turmas participantes.
        self.turmas_participantes.append(turma)

    def exibir_informacoes(self):
        # Gera uma lista de strings com informações de cada turma participante.
        turmas_info = [turma.exibir_informacoes() for turma in self.turmas_participantes]
        # Retorna uma string formatada com o nome do campeonato e as turmas participantes.
        return f"Campeonato: {self.nome}, Turmas Participantes: {'; '.join(turmas_info)}"

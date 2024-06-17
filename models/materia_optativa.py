class MateriaOptativa:
    def __init__(self, nome, carga_horaria, responsavel, participantes=None):
        self.nome = nome  # Nome da matéria optativa.
        self.carga_horaria = carga_horaria  # Carga horária total da matéria.
        self.responsavel = responsavel  # Pessoa responsável pela matéria.
        self.participantes = participantes if participantes else []  # Lista de participantes, se fornecida, ou lista vazia.

    def exibir_informacoes(self):
        # Gera uma string com os nomes e matrículas dos participantes.
        participantes_nomes = [f"{participante.nome} ({participante.matricula})" for participante in self.participantes]
        # Retorna uma descrição formatada da matéria optativa.
        return f"Matéria: {self.nome}, Carga Horária: {self.carga_horaria}, Responsável: {self.responsavel}, Participantes: {', '.join(participantes_nomes)}"

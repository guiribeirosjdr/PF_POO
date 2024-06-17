class Turma:
    def __init__(self, nome, curso_nome, professor, alunos):
        # Inicializa os atributos da turma
        self.nome = nome
        self.curso_nome = curso_nome
        self.professor = professor
        self.alunos = alunos
        # Inicializa os dicionários de notas e presenças para cada aluno
        self.notas = {aluno.matricula: [] for aluno in alunos}
        self.presencas = {aluno.matricula: [] for aluno in alunos}

    def exibir_informacoes(self):
        # Retorna uma string com as informações da turma
        return f"Turma: {self.nome}, Curso: {self.curso_nome}, Professor: {self.professor.nome}"

    def lancar_nota(self, aluno, nota):
        # Lança uma nota para o aluno
        if aluno.matricula not in self.notas:
            self.notas[aluno.matricula] = []
        self.notas[aluno.matricula].append(nota)

    def lancar_presenca(self, aluno, presente):
        # Lança a presença do aluno (presente ou ausente)
        self.presencas[aluno.matricula].append(presente)

    def calcular_media(self, aluno):
        # Calcula a média das notas do aluno
        notas_aluno = self.notas.get(aluno.matricula, [])
        if notas_aluno:
            return sum(notas_aluno) / len(notas_aluno)
        return 0.0

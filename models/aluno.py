class Aluno:
    def __init__(self, nome, idade, matricula, email):
        # Inicializa um aluno com informações básicas e estruturas para armazenar notas e presenças.
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.email = email
        self.notas = []  # Lista para armazenar notas.
        self.total_aulas = 0  # Contador de aulas para cálculo de frequência.
        self.presencas = 0  # Contador de presenças.
        self.historico_escolar = []  # Lista para armazenar histórico escolar.

    def adicionar_nota(self, nota):
        # Adiciona uma nota à lista de notas do aluno.
        self.notas.append(nota)

    def calcular_media(self):
        # Calcula a média das notas do aluno ou retorna 0 se não houver notas.
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def registrar_presenca(self):
        # Incrementa o contador de presenças.
        self.presencas += 1

    def registrar_aula(self):
        # Incrementa o contador de aulas totais.
        self.total_aulas += 1

    def calcular_frequencia(self):
        # Calcula a frequência de presença às aulas em percentual.
        return (self.presencas / self.total_aulas) * 100 if self.total_aulas > 0 else 0

    def verificar_aprovacao(self):
        # Verifica se o aluno está aprovado com base na média de notas e frequência de presença.
        media_aprovada = self.calcular_media() >= 60
        frequencia_aprovada = self.calcular_frequencia() >= 75
        return media_aprovada and frequencia_aprovada

    def solicitar_historico(self):
        # Retorna o histórico escolar do aluno como uma string formatada.
        return "\n".join(self.historico_escolar)

    def exibir_informacoes(self):
        # Retorna informações do aluno formatadas, incluindo status de aprovação.
        status = "Aprovado" if self.verificar_aprovacao() else "Reprovado"
        return f"Aluno: {self.nome}, Matrícula: {self.matricula}, Média: {self.calcular_media()}, Frequência: {self.calcular_frequencia()}%, Status: {status}, Email: {self.email}"

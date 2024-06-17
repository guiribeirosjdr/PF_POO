class Matricula:
    def __init__(self, aluno, turma, data_matricula):
        self.aluno = aluno  # Objeto representando o aluno matriculado.
        self.turma = turma  # Objeto representando a turma na qual o aluno está matriculado.
        self.data_matricula = data_matricula  # Data em que a matrícula foi realizada.
        self.status_pagamento = "Pendente"  # Estado inicial do pagamento da matrícula.

    def efetuar_pagamento(self):
        # Atualiza o status do pagamento para "Pago".
        self.status_pagamento = "Pago"

    def verificar_status(self):
        # Retorna o status atual do pagamento.
        return self.status_pagamento

    def exibir_informacoes(self):
        # Retorna uma string formatada com as informações detalhadas da matrícula.
        return f"Matrícula: Aluno: {self.aluno.nome}, Turma: {self.turma.identificador}, Data: {self.data_matricula}, Status: {self.status_pagamento}"

class Funcionario:
    def __init__(self, nome, cargo, horario, email):
        self.nome = nome  # Nome do funcionário.
        self.cargo = cargo  # Cargo que o funcionário ocupa.
        self.horario = horario  # Horário de trabalho do funcionário.
        self.email = email  # Email do funcionário.

    def exibir_informacoes(self):
        # Retorna uma string formatada com as informações do funcionário.
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}, Horário: {self.horario}, Email: {self.email}"

from models.pessoa import Pessoa  # Importa a classe Pessoa do módulo models.pessoa para utilizar como superclasse.

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, horario, email):
        super().__init__(nome, idade)  # Chama o construtor da superclasse Pessoa.
        self.cargo = cargo  # Cargo que o funcionário ocupa.
        self.horario = horario  # Horário de trabalho do funcionário.
        self.email = email  # Email do funcionário.

    def exibir_informacoes(self):
        # Retorna uma string formatada com as informações do funcionário.
        return f"Funcionário: {self.nome}, Idade: {self.idade}, Cargo: {self.cargo}, Horário: {self.horario}, Email: {self.email}"

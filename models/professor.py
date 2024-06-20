from models.pessoa import Pessoa  # Importa a classe Pessoa do módulo models.pessoa para utilizar como superclasse.

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplinas, email):
        super().__init__(nome, idade)  # Chama o construtor da superclasse Pessoa.
        self.disciplinas = disciplinas  # Lista de disciplinas que o professor leciona.
        self.email = email  # Email do professor.

    def exibir_informacoes(self):
        # Método para exibir informações formatadas sobre o professor.
        return f"Professor: {self.nome}, Idade: {self.idade}, Disciplinas: {self.disciplinas}, Email: {self.email}"

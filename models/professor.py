class Professor:
    def __init__(self, nome, idade, disciplinas, email):
        self.nome = nome  # Nome do professor.
        self.idade = idade  # Idade do professor.
        self.disciplinas = disciplinas  # Lista de disciplinas que o professor leciona.
        self.email = email  # Email do professor.

    def exibir_informacoes(self):
        # Método para exibir informações formatadas sobre o professor.
        return f"Professor: {self.nome}, Idade: {self.idade}, Disciplinas: {self.disciplinas}, Email: {self.email}"

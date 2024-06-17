class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros da biblioteca.
        self.reservas = []  # Lista para armazenar reservas de livros.

    def adicionar_livro(self, livro):
        # Adiciona um livro à coleção da biblioteca.
        self.livros.append(livro)

    def remover_livro(self, livro):
        # Remove um livro da coleção, se ele existir.
        if livro in self.livros:
            self.livros.remove(livro)

    def listar_livros(self):
        # Retorna uma string com todos os livros listados, um por linha.
        return "\n".join(self.livros)

    def reservar_livro(self, livro, aluno):
        # Adiciona uma reserva se o livro está disponível na coleção.
        if livro in self.livros:
            self.reservas.append((livro, aluno))

    def listar_reservas(self):
        # Retorna uma string com todas as reservas listadas, com informações do livro e do aluno.
        return "\n".join([f"Livro: {livro}, Aluno: {aluno.nome}" for livro, aluno in self.reservas])

    def excluir_reserva(self, livro, aluno):
        # Remove uma reserva específica, se ela existir.
        reserva = (livro, aluno)
        if reserva in self.reservas:
            self.reservas.remove(reserva)

from datetime import datetime

class Reserva:
    def __init__(self, turma, inicio, fim):
        self.turma = turma  # Referência à turma associada à reserva.
        self.inicio = inicio  # Data/hora de início da reserva.
        self.fim = fim  # Data/hora de término da reserva.

    def __str__(self):
        # Método para retornar uma representação em string da reserva.
        return f"Reserva para {self.turma} de {self.inicio} até {self.fim}"

class Seguranca:
    def __init__(self):
        self.rondas = []  # Lista para armazenar registros de rondas.

    def iniciar_ronda(self, funcionario):
        # Registra o início de uma ronda por um funcionário específico.
        self.rondas.append(f"Ronda iniciada por {funcionario.nome}")
        return f"Ronda iniciada por {funcionario.nome}"

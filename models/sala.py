from models.reserva import Reserva

class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero  # Identificador da sala.
        self.capacidade = capacidade  # Capacidade máxima de pessoas.
        self.reservas = []  # Lista para manter o controle das reservas.

    def reservar(self, turma, inicio, fim):
        # Cria uma nova reserva e verifica se não há conflitos antes de adicioná-la à lista.
        nova_reserva = Reserva(turma, inicio, fim)
        if self.verificar_disponibilidade(inicio, fim):
            self.reservas.append(nova_reserva)
            return True
        return False

    def verificar_disponibilidade(self, inicio, fim):
        # Verifica se a sala está disponível para reserva no intervalo especificado.
        for reserva in self.reservas:
            if not (fim <= reserva.inicio or inicio >= reserva.fim):
                return False
        return True

    def exibir_informacoes(self):
        # Retorna informações da sala, incluindo todas as reservas associadas.
        reservas_info = "\n".join(str(reserva) for reserva in self.reservas)
        return f"Sala: {self.numero}, Capacidade: {self.capacidade}\nReservas:\n{reservas_info}"

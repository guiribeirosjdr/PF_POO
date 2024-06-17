class Evento:
    def __init__(self):
        self.eventos = []  # Lista para armazenar eventos como dicionários.

    def adicionar_evento(self, nome, data, local):
        # Adiciona um novo evento à lista e envia um lembrete automaticamente.
        self.eventos.append({'nome': nome, 'data': data, 'local': local})
        self.enviar_lembrete(nome, data, local)

    def listar_eventos(self):
        # Retorna uma string formatada com os detalhes de todos os eventos.
        return "\n".join([f"Nome: {evento['nome']}, Data: {evento['data']}, Local: {evento['local']}" for evento in self.eventos])

    def enviar_lembrete(self, nome, data, local):
        # Imprime um lembrete sobre o evento.
        print(f"Lembrete: Evento '{nome}' em {data} no local {local}.")

    def remover_evento(self, nome):
        # Remove eventos pelo nome.
        self.eventos = [evento for evento in self.eventos if evento['nome'] != nome]

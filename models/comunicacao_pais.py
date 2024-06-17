class ComunicacaoPais:
    def __init__(self):
        # Inicializa a lista de pessoas
        self.pessoas = []

    def adicionar_pessoa(self, pessoa):
        # Adiciona uma pessoa à lista de pessoas
        self.pessoas.append(pessoa)

    def enviar_mensagem(self, email, mensagem):
        # Simula o envio de uma mensagem para um endereço de e-mail
        print(f"Enviando mensagem para {email}: {mensagem}")
        # Confirma o envio da mensagem
        self.confirmar_envio()

    def confirmar_envio(self):
        # Imprime uma mensagem de confirmação de envio
        print("Mensagem enviada com sucesso!")

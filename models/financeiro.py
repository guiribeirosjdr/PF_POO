class Financeiro:
    def __init__(self):
        self.receitas = []  # Lista para armazenar informações de receitas.
        self.despesas = []  # Lista para armazenar informações de despesas.

    def registrar_pagamento(self, nome, valor):
        # Adiciona um registro de receita à lista.
        self.receitas.append({'nome': nome, 'valor': valor})

    def registrar_despesa(self, nome, valor):
        # Adiciona um registro de despesa à lista.
        self.despesas.append({'nome': nome, 'valor': valor})

    def exibir_informacoes(self):
        # Cria strings formatadas listando todas as receitas e despesas registradas.
        receitas_info = "\n".join([f"{receita['nome']}: R${receita['valor']:.2f}" for receita in self.receitas])
        despesas_info = "\n".join([f"{despesa['nome']}: R${despesa['valor']:.2f}" for despesa in self.despesas])
        return f"Receitas:\n{receitas_info}\n\nDespesas:\n{despesas_info}"

class Inventario:
    def __init__(self):
        self.itens = {}  # Dicionário para armazenar itens e suas quantidades.

    def adicionar_item(self, item, quantidade):
        # Adiciona uma quantidade de um item ao inventário. Se o item já existe, aumenta a quantidade.
        if item in self.itens:
            self.itens[item] += quantidade
        else:
            self.itens[item] = quantidade

    def remover_item(self, item, quantidade):
        # Remove uma quantidade de um item do inventário, se possível. Remove o item do dicionário se a quantidade chegar a zero.
        if item in self.itens and self.itens[item] >= quantidade:
            self.itens[item] -= quantidade
            if self.itens[item] == 0:
                del self.itens[item]

    def listar_itens(self):
        # Lista todos os itens no inventário com suas respectivas quantidades.
        return "\n".join([f"{item}: {quantidade}" for item, quantidade in self.itens.items()])

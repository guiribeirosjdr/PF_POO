class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # Atributo protegido para o nome.
        self._idade = idade  # Atributo protegido para a idade.

    @property
    def nome(self):
        # Getter para o nome.
        return self._nome

    @nome.setter
    def nome(self, nome):
        # Setter para o nome, permite modificação direta do nome.
        self._nome = nome

    @property
    def idade(self):
        # Getter para a idade.
        return self._idade

    @idade.setter
    def idade(self, idade):
        # Setter para a idade, permite modificação direta da idade.
        self._idade = idade

    def exibir_informacoes(self):
        # Método abstrato para exibir informações; deve ser implementado por subclasses.
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses.")

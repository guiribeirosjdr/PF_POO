import pickle

def carregar_dados(caminho):
    try:
        # Tenta abrir o arquivo especificado no modo de leitura binária
        with open(caminho, 'rb') as f:
            # Carrega e retorna os dados do arquivo usando pickle
            return pickle.load(f)
    except FileNotFoundError:
        # Se o arquivo não for encontrado, retorna uma lista de objetos padrão
        return [], [], [], [], [], [], [], [], Financeiro(), [], Biblioteca(), Seguranca(), [], [], [], []

def salvar_dados(caminho, dados):
    # Abre o arquivo especificado no modo de escrita binária
    with open(caminho, 'wb') as f:
        # Salva os dados no arquivo usando pickle
        pickle.dump(dados, f)

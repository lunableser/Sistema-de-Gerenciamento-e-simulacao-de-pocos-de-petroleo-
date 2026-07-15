# SISTEMA DE GERENCIAMENTO E SIMULAÇÃO DE POÇOS DE PETRÓLEO EM PYTHON 
# classe do poço de petróleo - a qual define os atributos

class Poco:

    def __init__(self, id_poco, campo, declinio, senha, producao):

        self.id = id_poco          # identificação do poço
        self.campo = campo        # localização/campo de produção
        self.declinio = declinio  # taxa anual de declínio
        self.senha = senha        # senha do operador
        self.producao = producao  # produção acumulada em barris

        
from src.models.memoriaFisicaModel import MemoriaFisicaModel
from src.models.memoriaVirtualModel import MemoriaVirtualModel

"""
    tabela de paginação vai ser um vetor onde cada item é uma pagina que contem uma pagina do processo
    
"""

class gerenciadorMemoriaModel(): 
    def __init__(self, memoria_virtual: MemoriaVirtualModel  = None, memoria_fisica: MemoriaFisicaModel = None):
        self.memoria_virtual = memoria_virtual
        self.memoria_fisica = memoria_fisica
        self.memoria_fifo = []
        self.tabela_de_referencia = [{"pagina_logica":1, "pagina_fisica": 3}, {}, {}]
    
    def busca_endereco_fisico(self, pagina_logica):
        pagina_memoria_logica = self.memoria_virtual.busca_pagina(self.tabela_de_referencia[pagina_logica-1]["pagina_logica"])
        pagina_memoria_fisica = self.memoria_fisica.busca_pagina(self.tabela_de_referencia[pagina_logica-1]["pagina_fisica"])
        
        for pagina_logica in pagina_memoria_logica:
            pass
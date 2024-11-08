from abc import ABC
import rich
from utils.loggerUtils import LoggerUtils
"""
cada memoria vai ser um vetor
cada item do vetor vai corresponder a uma pagina
"""

[["","",""], ["", "", ""]]

class MemoriaAbstrata(ABC):
    def __init__(self):
        super().__init__()
        self.memoria = []
        self.logger = LoggerUtils()
        self.numero_padrao_colunas = 0
        self.nome_memoria = ""
        self.logger = LoggerUtils()
        
    def busca_pagina(self, pagina):
        if(pagina > len(self.memoria) or pagina < 0):
            self.logger.error("Numero de paginas invalido.")
            return {"pagina":None, "index":possicao_memoria_sendo_acessado, "acessado":False}
        possicao_memoria_sendo_acessado = pagina-1
        try:
            return {"pagina":self.memoria[possicao_memoria_sendo_acessado], "index":possicao_memoria_sendo_acessado, "acessado": True}
        except IndexError:
            return {"pagina":None, "index":possicao_memoria_sendo_acessado, "acessado":False}
        
    def printa_memoria(self):
        print("")
        self.logger.table(self.nome_memoria, self.memoria, self.numero_padrao_colunas)
        print("")
    
            
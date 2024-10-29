from abc import ABC

"""
cada memoria vai ser um vetor
cada item do vetor vai corresponder a uma pagina
cada pagina vai ter um dicionario correspondendo ao processo
"""

[["","",""], ["", "", ""]]

class MemoriaAbstrata(ABC):
    def __init__(self, numero_de_byte: int):
        super().__init__()
        self.numero_paginas = numero_de_byte
        self.memoria = []
        
    def busca_pagina(self, pagina):
        if(pagina > self.numero_paginas or pagina < 0):
            raise Exception("Numero de paginas invalido.")
        possicao_memoria_sendo_acessado = pagina-1
        try:
            return {"pagina":self.memoria[possicao_memoria_sendo_acessado], "index":possicao_memoria_sendo_acessado, "acessado": True}
        except IndexError:
            return {"pagina":None, "index":possicao_memoria_sendo_acessado, "acessado":False}
    
            
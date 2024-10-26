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
        if(pagina > self.numero_paginas):
            raise Exception("Numero de paginas invalido.")
        return self.memoria[pagina-1]
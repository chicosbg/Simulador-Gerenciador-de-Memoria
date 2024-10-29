from abstratos.memoriaAbstrata import MemoriaAbstrata

class MemoriaVirtualModel(MemoriaAbstrata):
    def __init__(self):
        super().__init__(numero_paginas=3)
        self.memoria = []
    
    def adiciona_lista_de_paginas(self, lista_paginas):
        self.memoria = lista_paginas    
from abstratos.memoriaAbstrata import MemoriaAbstrata

class MemoriaVirtualModel(MemoriaAbstrata):
    def __init__(self, numero_paginas):
        super().__init__(numero_paginas=numero_paginas)
        self.memoria = []
    
    def adiciona_lista_de_paginas(self, lista_paginas):
        self.memoria = lista_paginas    
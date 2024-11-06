from abstratos.memoriaAbstrata import MemoriaAbstrata
import math

class MemoriaVirtualModel(MemoriaAbstrata):
    def __init__(self, tam_memoria_bytes):
        super().__init__()
        quantidades_de_paginas = math.log(tam_memoria_bytes, 2)
        self.numero_paginas = quantidades_de_paginas
        self.memoria = []
    
    def adiciona_lista_de_paginas(self, lista_paginas):
        self.memoria = lista_paginas 
    def get_numero_paginas(self):
        return self.numero_paginas
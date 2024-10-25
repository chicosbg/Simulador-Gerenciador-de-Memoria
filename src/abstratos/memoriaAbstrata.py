from abc import ABC

class MemoriaAbstrata(ABC):
    numero_paginas = 2
    def __init__(self, numero_de_bits: int):
        self.numero_paginas = self.numero_paginas^numero_de_bits
        pass
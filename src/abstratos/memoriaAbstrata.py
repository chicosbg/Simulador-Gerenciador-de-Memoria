from abc import ABC

class MemoriaAbstrata(ABC):
    def __init__(self, numero_de_bits: int):
        super().__init__()
        self.numero_paginas = 2^numero_de_bits
        pass
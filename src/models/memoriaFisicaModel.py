from abstratos.memoriaAbstrata import MemoriaAbstrata
class MemoriaVirtualModel(MemoriaAbstrata):
    def __init__(self):
        super().__init__(numero_de_bits=16)
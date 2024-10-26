from abstratos.memoriaAbstrata import MemoriaAbstrata

class MemoriaVirtualModel(MemoriaAbstrata):
    def __init__(self):
        super().__init__(numero_de_byte=16)
        self.memoria = [["t","e","f"], ["e","f", "g"], ["t", "k", "l"]]
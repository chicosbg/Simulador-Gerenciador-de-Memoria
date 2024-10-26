from abstratos.memoriaAbstrata import MemoriaAbstrata

class MemoriaFisicaModel(MemoriaAbstrata):
    def __init__(self):
        super().__init__(numero_de_byte=16)
        self.memoria = [["e","f", "g"], ["t", "k", "l"], ["t","e","f"]]
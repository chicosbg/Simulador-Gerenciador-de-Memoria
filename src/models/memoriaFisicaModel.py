from abstratos.memoriaAbstrata import MemoriaAbstrata
class MemoriaFisicaModel(MemoriaAbstrata):
    def __init__(self):
        super().__init__(numero_de_bits=16)
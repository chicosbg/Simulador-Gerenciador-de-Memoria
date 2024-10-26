from src.models.memoriaFisicaModel import MemoriaFisicaModel
from src.models.memoriaVirtualModel import MemoriaVirtualModel

class gerenciadorMemoriaModel(): 
    def __init__(self, memoria_virtual: MemoriaVirtualModel  = None, memoria_fisica: MemoriaFisicaModel = None):
        self.memoria_virtual = memoria_virtual
        self.memoria_fisica = memoria_fisica
    
    def acha_endereco_fisico(self,): 
        pass
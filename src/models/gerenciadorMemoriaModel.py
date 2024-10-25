from abstratos.memoriaAbstrata import MemoriaAbstrata

class gerenciadorMemoriaModel(MemoriaAbstrata): 
    def __init__(self):
        self.numero_paginas = self.numero_paginas^16
        super().__init__(self=self)
    
    def acha_endereco_fisico(self, memoria_virtual, memoria_fisica): 
        pass
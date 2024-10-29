from models.memoriaFisicaModel import MemoriaFisicaModel
from models.memoriaVirtualModel import MemoriaVirtualModel

"""
    tabela de paginação vai ser um vetor onde cada item é uma pagina que contem uma pagina do processo
    
"""

class gerenciadorMemoriaModel(): 
    def __init__(self, memoria_virtual: MemoriaVirtualModel  = None, memoria_fisica: MemoriaFisicaModel = None):
        self.memoria_virtual = memoria_virtual
        self.memoria_fisica = memoria_fisica
        if memoria_virtual == None:
            self.memoria_virtual = MemoriaVirtualModel()
        if memoria_fisica == None:
            self.memoria_fisica = MemoriaFisicaModel()
        
        self.memoria_fifo = []
        self.tabela_de_referencia = [{"pagina_logica":1, "pagina_fisica": 3}, {}, {}]
    
    def acessa_paginas(self, pagina_logica):
        if(pagina_logica < 1):
            raise Exception("Numero da pagina invalido.")
        posicao_pagina_logica = self.tabela_de_referencia[pagina_logica-1]["pagina_logica"]
        posicao_pagina_fisica = self.tabela_de_referencia[pagina_logica-1]["pagina_fisica"]
        
        pagina_memoria_logica = self.memoria_virtual.busca_pagina(pagina=posicao_pagina_logica)
        if(not pagina_memoria_logica["acessado"]):
            print(f"Posicao na memoria virtual \"{pagina_logica}\" invalido.")
            return
        
        pagina_memoria_fisica = self.memoria_fisica.busca_pagina(pagina=posicao_pagina_fisica)

        if(not pagina_memoria_fisica["acessado"]):
            print(f"Ocorreu um page fault na referencia: {self.tabela_de_referencia[pagina_logica-1]}")
            self._trata_page_fault(pagina_memoria_logica==pagina_memoria_logica["pagina"])
            return
        
        print(f"verificando se a {pagina_logica} está presente no quadro {posicao_pagina_fisica} da memoria fisica.")
        
    def _trata_page_fault(self, pagina_memoria_logica):
        self.memoria_fisica.adiciona_na_memoria_fisica(pagina_memoria_logica)
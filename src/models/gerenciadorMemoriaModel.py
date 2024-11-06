from models.memoriaFisicaModel import MemoriaFisicaModel
from models.memoriaVirtualModel import MemoriaVirtualModel

"""
    tabela de paginação vai ser um vetor onde cada item é uma pagina que contem uma pagina do processo
    
"""

class gerenciadorMemoriaModel(): 
    def __init__(self, memoria_virtual: MemoriaVirtualModel  = None, memoria_fisica: MemoriaFisicaModel = None):
        self.memoria_virtual = memoria_virtual
        self.memoria_fisica = memoria_fisica
        self.numero_page_fault = 0
        self.tabela_de_referencia = [{"pagina_logica":-1, "quadro_fisico": -1}]
        memoria_fisica.set_numero_quadros(memoria_virtual.get_numero_paginas())
    
    def acessa_paginas(self, posicao_pagina):
        if(posicao_pagina < 1):
            raise Exception("Numero da pagina invalido.")

        posicao_referencia_ml_mf = self._procura_referencia_pagina_logica(pagina_logica=posicao_pagina)

        foi_alocado_na_memoria_fisica = posicao_referencia_ml_mf != -1

        posicao_pagina_fisica = None
        
        if(foi_alocado_na_memoria_fisica):
            posicao_pagina_fisica = self.tabela_de_referencia[posicao_referencia_ml_mf]["pagina_fisica"]
        
        pagina_memoria_logica = self.memoria_virtual.busca_pagina(pagina=posicao_pagina)
        if(not pagina_memoria_logica["acessado"]):
            print(f"Posicao da pagina na memoria virtual \"{posicao_pagina}\" invalido.")
            return
        
        pagina_memoria_fisica = {"acessado": False}
        
        if(foi_alocado_na_memoria_fisica):
            pagina_memoria_fisica = self.memoria_fisica.busca_pagina(pagina=posicao_pagina_fisica)

        if(not pagina_memoria_fisica["acessado"] or pagina_memoria_logica["pagina"] != pagina_memoria_fisica["pagina"]):
            if(self.numero_page_fault == 0):
                self.tabela_de_referencia.pop(0)
            self.numero_page_fault += 1
            print(f"Ocorreu um page fault com o a posicação virtual {posicao_pagina}")
            self._trata_page_fault(pagina_memoria_logica=pagina_memoria_logica["pagina"], posicao_memoria_logica=pagina_memoria_logica["index"]+1, posicao_da_referencia=posicao_referencia_ml_mf)
            return
        
        
    def _trata_page_fault(self, pagina_memoria_logica, posicao_memoria_logica, posicao_da_referencia):
        posicao_inserida = self.memoria_fisica.adiciona_na_memoria_fisica(pagina_memoria_logica)
        if(posicao_da_referencia == -1):
            self.tabela_de_referencia.append({"pagina_logica": posicao_memoria_logica, "pagina_fisica":posicao_inserida})
            return
        self.tabela_de_referencia[posicao_da_referencia]["pagina_fisica"] = posicao_inserida
    
    def _procura_referencia_pagina_logica(self, pagina_logica):
        for index, referencia in enumerate(self.tabela_de_referencia):
            if(referencia["pagina_logica"] == pagina_logica):
                return index
        return -1
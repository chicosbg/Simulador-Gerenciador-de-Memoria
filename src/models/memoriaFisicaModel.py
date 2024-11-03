from abstratos.memoriaAbstrata import MemoriaAbstrata

class MemoriaFisicaModel(MemoriaAbstrata):
    def __init__(self, tam_memoria_bytes):
        super().__init__(tam_memoria_bytes=tam_memoria_bytes)
        self.memoria = []
        self.fila_de_quadros = []
        
    def adiciona_na_memoria_fisica(self, pagina_memoria_logica):
        if(len(self.memoria) < self.numero_paginas):
            self.memoria.append(pagina_memoria_logica)
            index_inserido = len(self.memoria)
            print(len(self.memoria))
            self.fila_de_quadros.append(index_inserido)
            return index_inserido
        
        mais_antigo_da_fila = self.fila_de_quadros.pop(0)
        self.memoria[mais_antigo_da_fila-1] = pagina_memoria_logica
        self.fila_de_quadros.append(mais_antigo_da_fila)
        return mais_antigo_da_fila
        
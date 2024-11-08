from abstratos.memoriaAbstrata import MemoriaAbstrata
import math
class MemoriaFisicaModel(MemoriaAbstrata):
    def __init__(self, tam_max_quadros):
        super().__init__()
        self.memoria = []
        self.fila_de_quadros = []
        self.tam_max_quadros = int(tam_max_quadros)
        self.tam_memoria_bytes = self.tam_max_quadros*4
        self.nome_memoria = "Memoria Fisica"
        self.numero_padrao_colunas = self.tam_max_quadros
        
    def adiciona_na_memoria_fisica(self, pagina_memoria_logica):
        #verifica se a memoria não está cheia, então adiciona na memoria e add na fila
        if(self.memoria_nao_esta_cheia()):
            self.memoria.append(pagina_memoria_logica)
            index_inserido = len(self.memoria)
            self.fila_de_quadros.append(index_inserido)
            return index_inserido
        # logica de FIFO
        mais_antigo_da_fila = self.fila_de_quadros.pop(0)
        self.memoria[mais_antigo_da_fila-1] = pagina_memoria_logica
        self.fila_de_quadros.append(mais_antigo_da_fila)
        return mais_antigo_da_fila
    
    def set_numero_quadros(self, tam_paginas):
        self.tam_max_quadros = math.floor(self.tam_memoria_bytes/tam_paginas)
        
    def get_numero_quadros(self):
        return self.tam_max_quadros
    
    def memoria_nao_esta_cheia(self):
        return len(self.memoria) <= self.tam_max_quadros

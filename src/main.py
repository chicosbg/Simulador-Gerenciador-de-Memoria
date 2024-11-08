from models.gerenciadorMemoriaModel import gerenciadorMemoriaModel
from models.memoriaFisicaModel import MemoriaFisicaModel
from models.memoriaVirtualModel import MemoriaVirtualModel
from utils.loggerUtils import LoggerUtils
import random
import signal
import os
# Tamanho de quadro/página: 4 bytes ou 32 bits

def handle_sigint(signum, frame):
        print("\nEncerrando sistema...")
        exit(0)

log = LoggerUtils()

log.info("Inicio da operacao")

memoria_fisica = MemoriaFisicaModel(tam_max_quadros=3)
memoria_virtual = MemoriaVirtualModel(numero_de_paginas=6)
memoria_virtual.adiciona_lista_de_paginas([["t","e","f","a"], ["e","f","g","a"], ["t","k","l","a"], ["t","k","l","a"], ["v","v","l","v"], ["t","t","s","r"]])
arq = gerenciadorMemoriaModel(memoria_fisica=memoria_fisica, memoria_virtual=memoria_virtual)

# memoria_virtual.printa_memoria()
# memoria_fisica.printa_memoria()

signal.signal(signal.SIGINT, handle_sigint)

while (True):
    print("-"*20)
    endereco_inteiro = random.randint(0, memoria_virtual.numero_paginas*4 - 1)
    endereco_binario = f'{endereco_inteiro:0{8}b}'
    pagina = int(endereco_binario[0:6], 2) + 1      # 6 bits mais significativos
    deslocamento = int(endereco_binario[6:8], 2)    # 2 bits menos significativos
    
    log.info(f"Endereço gerado: {endereco_binario}")
    log.info(f"Página: {pagina}, Deslocamento: {deslocamento}")    
    log.info(f"Total de page fault {arq.get_numero_page_fault()}")    
    
    arq.acessa_paginas(posicao_pagina=pagina)

    memoria_virtual.printa_memoria()
    memoria_fisica.printa_memoria()
    
    input()
    os.system('clear')

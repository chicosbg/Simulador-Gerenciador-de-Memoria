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

if __name__ == "__main__":
        log = LoggerUtils()

        tam_memoria_fisica = int(input("Insira o número de molduras (memória física): "))
        tam_memoria_virtual = int(input("Insira o número de páginas (memória virtual): "))
        arquivo_acessos = input("Insira o caminho para o arquivo: ")
        modo_aleatorio = False

        if tam_memoria_fisica > 64 or tam_memoria_virtual > 64:
                print("Tamanho máximo de memória: 64 páginas/molduras")
                exit(0)
        
        if arquivo_acessos == "":
                modo_aleatorio = True

        log.info("Inicio da operacao")

        memoria_fisica = MemoriaFisicaModel(tam_max_quadros=tam_memoria_fisica)
        memoria_virtual = MemoriaVirtualModel(numero_de_paginas=tam_memoria_virtual)

        i = 0 
        lista_paginas = []
        while(i<tam_memoria_virtual):
                caracteres = [chr(random.randint(32, 126)), chr(random.randint(32, 126)), chr(random.randint(32, 126)), chr(random.randint(32, 126))]
                lista_paginas.append(caracteres)
                i += 1

        memoria_virtual.adiciona_lista_de_paginas(lista_paginas)
        arq = gerenciadorMemoriaModel(memoria_fisica=memoria_fisica, memoria_virtual=memoria_virtual)

        signal.signal(signal.SIGINT, handle_sigint)

        if modo_aleatorio:
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
                        # os.system('clear')
        else:
                buffer = None
                try:
                        with open(arquivo_acessos, "r") as arquivo:

                                for linha in arquivo:
                                        binario = linha.strip()

                                        if(len(binario) == 8 and all(char in '01' for char in binario)):
                                                log.info(f"Endereço lido: {binario}")
                                                pagina = int(binario[0:6], 2) + 1
                                                deslocamento = int(binario[6:8], 2)

                                                log.info(f"Página: {pagina}, Deslocamento: {deslocamento}")    
                                                log.info(f"Total de page fault {arq.get_numero_page_fault()}")    

                                                arq.acessa_paginas(posicao_pagina=pagina)

                                                memoria_virtual.printa_memoria()
                                                memoria_fisica.printa_memoria()
                                        
                                                input()
                                                # os.system('clear')
                                        else:
                                                raise Exception("Formatação inválida do arquivo")
                except Exception as error:
                        print(error)

                print("Fim da execução")

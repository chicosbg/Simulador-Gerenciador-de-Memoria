from models.gerenciadorMemoriaModel import gerenciadorMemoriaModel
from models.memoriaFisicaModel import MemoriaFisicaModel
from models.memoriaVirtualModel import MemoriaVirtualModel

memoria_fisica = MemoriaFisicaModel(tam_memoria_bytes=32)
memoria_virtual = MemoriaVirtualModel(tam_memoria_bytes=32)
memoria_virtual.adiciona_lista_de_paginas([["t","e","f"], ["e","f", "g"], ["t", "k", "l"]])
arq = gerenciadorMemoriaModel(memoria_fisica=memoria_fisica, memoria_virtual=memoria_virtual)
memoria_virtual.printa_memoria()
memoria_fisica.printa_memoria()
print(arq.acessa_paginas(posicao_pagina=1))
print(arq.acessa_paginas(posicao_pagina=2))
print(arq.acessa_paginas(posicao_pagina=3))
print(arq.acessa_paginas(posicao_pagina=1))
memoria_virtual.printa_memoria()
memoria_fisica.printa_memoria()


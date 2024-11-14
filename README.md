# Sobre

O **Simulador-Gerenciador-de-Memoria** é um simulador de gerenciamento de memória com paginação de um sistema operacional. O gerenciamento de memória é o processo pelo qual o sistema operacional controla e organiza o uso da memória de um computador, assegurando que os programas em execução tenham acesso eficiente aos recursos de memória.

Existem dois tipos de abstração de memória no contexto do gerenciamento de memória em um sistema operacional:

- **Memória Física**: A memória física refere-se ao hardware real usado para armazenar os dados dos programas em um computador, ou seja, é a própria memória RAM em si.

- **Memória Virtual**: A memória virtual é uma abstração para todo o espaço de endereçamento de um programa.

Dividindo-se a memória física e virtual em paginas/molduras e utilizando as técnicas de gerenciamento, é possível executar programas que necessitem de mais espaço do que a memória física disponível.

# Pré-requisitos e instalação

O sistema é desenvolvido na linguagem __python__, que pode ser feito o download [aqui](https://www.python.org/downloads/)

Primeiramente deve ser clonado o repositório do projeto com o comando:

```$
git clone https://github.com/chicosbg/Simulador-Gerenciador-de-Memoria.git
```

Com repositório clonado instale as dependências (é obrigatório o pacote estar instalado):
```Bash
pip install -r ./requirements.txt
```

Acesse a pasta do projeto e execute o arquivo main.py:

```$
python3 src/main.py
```

# Funcionamento do Simulador

A cada passo na simulação o programa realiza as seguintes operações:

+ Gera um endereço lógico (endereço que vem do processador)
+ Calcula a página e o deslocamento de acordo com os bits do endereço
+ Exibe o endereço gerado, o número da página, do deslocamento e do total de page faults
+ Tenta acessar o endereço gerado na memória física
+ Imprime o conteúdo das memórias virtual e física

No início do programa deve-se especificar o tamanho da memória física e virtual em número de páginas.

# Arquitetura do Sistema

A arquitetura do simulador é composta pelos seguintes componentes: Memória Virtual, Memória Física, Gerenciador de Memória, ...

Cada página/moldura tem tamanho de 4 bytes

# Memória Abstrata

Define os atributos essenciais para o funcionamento do sistema como o atributo memoria que é abstraído como uma matriz de caracteres (bytes). Além disso define atributos acessórios para auxiliar na impressão do programa no terminal.

Também define métodos gerais que serão utilizados pelas classes derivadas: **MemoriaFisicaModel** e **MemoriaVirtualModel**.

# Memória Virtual

A memória virtual é implementada através da classe **MemoriaVirtualModel** e basicamente define um número de páginas para a memória virtual e um método para inicializar a essa memória.

# Memória Física

A memória física é implementada através da classe **MemoriaFisicaModel** definindo uma quantidade de molduras, chamadas de quadros e uma fila de molduras, necessária para o algoritmo da política de substituição (FIFO). Além disso um método para adicionar uma página da memória virtual na memória física.

# Gerenciador de Memória

O Gerenciador de Memória é implementado através da classe **GerenciadorMemoriaModel**, responsável pela manipulação das memórias física e virtual, realizando o acesso e verificando a ocorrência de page faults.

### Diagrama de classe
![Diagrama de classe](./docs/diagrama_de_classe.png)

### Fluxo do sistema
![Diagrama de fluxo](./docs/diagrama_simulador.png) 

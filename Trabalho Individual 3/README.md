# 🔹 Caminho Hamiltoniano em Python

##  Descrição do Projeto

Este projeto implementa em **Python** um algoritmo de **backtracking** para verificar se existe um **Caminho Hamiltoniano** em um grafo (direcionado ou não direcionado).  

Um **Caminho Hamiltoniano** é uma sequência de vértices onde **cada vértice do grafo é visitado exatamente uma vez**, sem repetições.

##  Como Executar o Projeto

###  Pré-requisitos
- Python 3.8 ou superior instalado.

###  Executar usando parâmetros
**Grafo não direcionado:**

python main.py --n 5 --arestas "0-1,1-2,2-3,3-4,0-4"

**Grafo direcionado:**

python main.py --n 4 --arestas "0>1,1>2,2>3"


**Escolher vértice inicial:**

python main.py --n 5 --arestas "0-1,1-2,2-3,3-4"

python main.py

###  Explicação do Algoritmo

O algoritmo tenta construir um caminho adicionando vértices não visitados.

Se todos os n vértices forem incluídos, o caminho Hamiltoniano foi encontrado.

Se ficar preso em um vértice sem saída → volta (backtracking) e tenta outro.

Se todas as tentativas falharem, não existe Caminho Hamiltoniano.

###  Relatório Técnico
####  1. Classes de Complexidade (P, NP, NP-Completo, NP-Difícil)
Problema	Classe
Verificar se um caminho dado é Hamiltoniano	P
Existe um Caminho Hamiltoniano no grafo?	NP-Completo
Versão de otimização (ex: maior caminho simples)	NP-Difícil

Este problema é relacionado diretamente com o Problema do Caixeiro Viajante (TSP), que também depende da existência de um ciclo Hamiltoniano.

####  2. Complexidade de Tempo do Algoritmo

O algoritmo testa combinações de vértices usando backtracking.

No pior caso, tenta todas as permutações possíveis de vértices.

Complexidade temporal aproximada:

O(n!)

Melhor caso: encontra na primeira tentativa → quase linear.

Caso médio: depende da densidade do grafo.

Pior caso: não existe caminho → explora o grafo inteiro.

#### 3. Teorema Mestre se aplica?

Não se aplica.
O Teorema Mestre exige recorrências do tipo:

T(n)=aT(n/b)+f(n)

Mas neste problema, a recursão não divide o grafo em subproblemas menores. Apenas tenta diferentes combinações (backtracking), logo não há subproblema T(n/b).

####  4. Melhores, Médios e Piores Casos
Caso	Situação	Complexidade
Melhor	Primeiro caminho tentado funciona	O(n)
Médio	Alguns retrocessos	Exponencial
Pior	Nenhum caminho existe	O(n!)

### Visualização do Grafo e Caminho Hamiltoniano

Este projeto também inclui um arquivo view.py, que permite desenhar o grafo e destacar o Caminho Hamiltoniano encontrado.

#### Pré-requisitos para visualizar

Instale as bibliotecas necessárias (somente se quiser visualizar o grafo):

pip install networkx matplotlib

#### Como executar o view.py
python view.py

Quando executar, será gerada uma imagem automaticamente.

Ela mostra:
- Todos os vértices do grafo
- Todas as arestas
- O Caminho Hamiltoniano destacado em negrito
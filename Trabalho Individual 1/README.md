# Algoritmo de Karatsuba em Python

##  Descrição do Projeto
Este projeto implementa o **algoritmo de Karatsuba**, criado por Anatolii Karatsuba em 1960, que permite multiplicar números inteiros grandes de forma mais eficiente do que a multiplicação tradicional.

O algoritmo reduz o número de multiplicações recursivas necessárias, alcançando complexidade de **O(n^log₂3) ≈ O(n^1.585)**, em contraste com a multiplicação tradicional que é **O(n²)**.

---

## 📂 Estrutura do Projeto
trabalho Individual 1/
│── main.py 
│── README.md

```bash

## ▶ Como Executar o Projeto

### 1. Clone o repositório
git clone https://github.com/seuusuario/trabalho_karatsuba.git
cd trabalho_karatsuba

### 2. Execute o projeto
python main.py

### 3. Informe dois numeros inteiros grandes
Digite o primeiro número: 12345678
Digite o segundo número: 87654321
Resultado da multiplicação: 1082152022374638


##  Relatorio Tecnico
### 1. Explicação da Lógica do Algoritmo

O algoritmo divide os números em duas partes e reduz a quantidade de multiplicações necessárias.

Exemplo simplificado:

Seja x = 1234 e y = 5678:

Divide em partes:

x = 12 | 34

y = 56 | 78

Calcula três produtos recursivos:

z0 = low_x * low_y

z1 = (low_x + high_x) * (low_y + high_y)

z2 = high_x * high_y

Combina os resultados na fórmula final:

resultado = (z2 * 10^(2*m)) + ((z1 - z2 - z0) * 10^m) + z0


Isso reduz de 4 multiplicações tradicionais para apenas 3 multiplicações recursivas.

### 2. Complexidade Ciclomática

A função karatsuba(x, y) possui os seguintes pontos de decisão:

if x < 10 or y < 10 (1 decisão)

chamadas recursivas (não adicionam novos ramos condicionais)

Fluxo de Controle Simplificado:

Início → Condição (x<10 ou y<10)?
 ├── Sim → retorna multiplicação direta
 └── Não → divide números, chama recursão e combina resultados


Número de nós (N): 4

Número de arestas (E): 5

Componentes conexos (P): 1

Cálculo:

M = E - N + 2P
M = 5 - 4 + 2*1
M = 3


 A complexidade ciclomática é 3, indicando baixa complexidade e fácil manutenção.

### 3. Complexidade Assintótica

Tempo:

Melhor caso: O(1) → quando os números são pequenos (x < 10 ou y < 10).

Caso médio/pior caso: O(n^log₂3) ≈ O(n^1.585).
(Mais eficiente que a multiplicação tradicional O(n²).)

Espaço:

O consumo de memória é O(n) devido ao uso da recursão e variáveis temporárias.

🎯 Conclusão

O algoritmo de Karatsuba é uma abordagem eficiente para multiplicação de números grandes, reduzindo o custo computacional em comparação ao método clássico.
Este projeto apresenta sua implementação em Python, juntamente com a análise de complexidade ciclomática e complexidade assintótica.
# Trabalho Individual 2 – MaxMin Select

## Descrição do Projeto
Este projeto implementa o algoritmo **MaxMin Select** utilizando **divisão e conquista**.  
O objetivo é encontrar simultaneamente o **maior** e o **menor** elemento de uma lista de números com **eficiência**, reduzindo o número de comparações em relação à abordagem ingênua.

---

## Como executar
Clone o repositório e rode o programa no Python:

```bash
git clone https://github.com/seuusuario/trabalho_individual_2_FPAA.git
cd trabalho individual 2
python main.py

🧠 Explicação da Lógica

O algoritmo segue os seguintes passos:

Divisão

O array é dividido em duas metades.

Cada metade é processada recursivamente.

Casos base

Se houver apenas um elemento, esse elemento é o mínimo e o máximo.

Se houver dois elementos, comparamos e determinamos o menor e o maior.

Combinação

Após resolver os subproblemas, os resultados são combinados pegando o menor dos mínimos e o maior dos máximos.

📊 Análise de Complexidade
🔹 Método de contagem de operações

Para cada divisão, são feitas 2 chamadas recursivas e no máximo 2 comparações (uma para mínimo, outra para máximo).

Para n elementos, o número total de comparações é ≤ 3n/2 – 2.

Assim, a complexidade é:

𝑇(𝑛)=𝑂(𝑛)
🔹 Aplicação do Teorema Mestre

A recorrência do algoritmo é:

𝑇(𝑛)=2𝑇(𝑛/2)+𝑂(1)

Identificando os parâmetros:
𝑎=2
𝑏=2
𝑓(𝑛)=𝑂(1)

Calculando:

log𝑏𝑎=log⁡22=1

Comparando 𝑓(𝑛) com 𝑛^log𝑏𝑎 = 𝑛^1:

f(n)=O(1), que é menor que n.

➡️ Portanto, aplica-se o Caso 1 do Teorema Mestre:

𝑇(𝑛)=𝑂(𝑛)

🖼️ Diagrama da Recursão

O diagrama abaixo mostra como o algoritmo divide o problema e combina os resultados:

![Diagrama MaxMin Select](/DiagramaMaxMin.png)

1. **Divisão do problema**  
   - O problema original com `n` elementos é dividido em duas metades (`n/2` cada).  
   - Esse processo continua até chegar nos **casos base**, onde restam apenas **1 ou 2 elementos**.  

2. **Combinação dos resultados**  
   - Em cada nível da árvore, após resolver os subproblemas, os resultados são **combinados**.  
   - São feitas **duas comparações principais**:  
     - Para encontrar o **mínimo global** entre os dois submínimos.  
     - Para encontrar o **máximo global** entre os dois submáximos.  

3. **Níveis da árvore e número de comparações**  
   - **Nível 0 (raiz)**: 1 problema de tamanho `n`.  
   - **Nível 1**: 2 subproblemas de tamanho `n/2`.  
   - **Nível 2**: 4 subproblemas de tamanho `n/4`.  
   - … e assim por diante, até atingir os casos base.  
   - Em cada nível, as combinações adicionam no máximo **2 comparações por nó**.  
   - O total de comparações é limitado por **≤ 3n/2 – 2**, mantendo a complexidade **O(n)**.  

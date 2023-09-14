## **Operações de convolução com máscaras**

Uma operação de convolução unidimensional entre dois vetores `A` e `B`, denotada por `A * B`, é como montar um vetor que contém os resultados da somas dos produtos de `A` por `B`, onde `B` é espelhado e deslocado sempre de posição para calcular o próximo valor de `A * B`, como na imagem a seguir, que assume A = {0, 1, 2, 3, 2, 1, 0} e B = {1, 3, -1}:

![tabela 2](./assets/tabela2.png)

Para matrizes bidimensionais, a ideia é a mesma. A máscara `B` será espelhada na horizontal e na vertical, deslocando-se linha por linha, por todas as linhas, até que percorra toda a matriz imagem `A`. O resultado será uma matriz do mesmo tamanho da matriz original. Para lidar com os pixels restantes, à borda da imagem que recebeu a máscara, podem-se usar muito métodos.
- 1. preencher com zeros o contorno da imagem, de maneira condizente com o tamanho 
de máscara utilizado, como ilustra a figura 18. 
- 2. preencher o contorno da imagem com os mesmos valores da(s) primeira(s) e última(s) 
linha(s) e coluna(s). 
- 3. prevenir a eventual introdução de erros nas regiões de bordas da imagem causados 
por qualquer um dos métodos acima, considerando na imagem resultante apenas os valores para 
os quais a máscara de convolução ficou inteiramente contida na imagem original.

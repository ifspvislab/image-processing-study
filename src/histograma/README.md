# Histograma de uma Imagem

O histograma de uma imagem é simplesmente um conjunto de números indicando o percentual de pixels naquela imagem que apresentam um determinado nível de cinza. Estes valores são normalmente representados por um gráfico de barras que fornece para cada nível de cinza o número (ou o percentual) de pixels correspondentes na imagem. Através da visualização do histograma de uma imagem obtemos uma indicação de sua qualidade quanto ao nível de contraste e quanto ao seu brilho médio (se a imagem é predominantemente clara ou escura).

Cada elemento deste conjunto é calculado como:

![](./assets/3.1.png)

onde:
- 0 ≤ 𝑟𝑘 ≤ 1
- 𝑘 = 0, 1, ..., 𝐿-1, onde 𝐿 é o número de níveis de cinza da imagem digitalizada.
- 𝑛 = número total de pixels na imagem.
- 𝑝𝑟(𝑟𝑘) = probabilidade do k-ésimo nível de cinza.
- 𝑛𝑘 = número de pixels cujo nível de cinza corresponde a k.

**Exemplo:**
Os dados da tabela 1 correspondem a uma imagem de 128 x 128 pixels, com 8 níveis de cinza. O número de pixels correspondentes a um certo tom de cinza está indicado na segunda coluna, enquanto as respectivas probabilidades 𝑝𝑟(𝑟𝑘) aparecem na terceira coluna. A representação gráfica equivalente deste histograma é mostrada na figura 1.

**Tabela 1 - Exemplo de histograma.**
Nível de cinza (𝑟𝑘) | 𝑛𝑘 | 𝑝𝑟(𝑟𝑘)
--- | --- | ---
0 | 1120 | 0,068
1/7 | 3214 | 0,196
2/7 | 4850 | 0,296
3/7 | 3425 | 0,209
4/7 | 1995 | 0,122
5/7 | 784 | 0,048
6/7 | 541 | 0,033
1 | 455 | 0,028
Total | 16384 | 1

![Exemplo de histograma para imagem com oito níveis de cinza.](./assets/fig1.png)

O conceito de histograma também é aplicável a imagens coloridas. Neste caso, a imagem é decomposta em seus componentes (por exemplo, R, G e B) e para cada componente é calculado o histograma correspondente.

Para computar o histograma de uma imagem monocromática, inicializa-se com zero todos os elementos de um vetor de 𝐿 elementos, onde 𝐿 é o número de tons de cinza possíveis. Em seguida, percorre-se a imagem, pixel a pixel, e incrementa-se a posição do vetor cujo índice corresponde ao tom de cinza do pixel visitado. Após toda a imagem ter sido percorrida, cada elemento do vetor conterá o número de pixels cujo tom de cinza equivale ao índice do elemento. Estes valores poderão ser normalizados, dividindo cada um deles pelo total de pixels na imagem.

**Concluindo:**
O histograma de uma imagem fornece diversas informações qualitativas e quantitativas sobre ela, como o nível de cinza mínimo, médio e máximo, predominância de pixels claros ou escuros, entre outros. No entanto, algumas conclusões qualitativas, como a qualidade subjetiva global da imagem, só podem ser extraídas ao observar a imagem propriamente dita.

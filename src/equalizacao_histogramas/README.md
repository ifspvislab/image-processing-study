## Equalização de Histograma

É uma técnica que busca redistribuir os valores de tons de cinza dos pixels em uma imagem para que seja obtido um histograma mais uniforme, utilizando-se a função abaixo, denominada como função de distribuição acumulada. 

<img src="/src/assets/formula-equalizacao1.png">
<img src="/src/assets/formula-equalizacao2.png">

Com essa função, primeiramente calculamos o valor equalizado para cada tom de cinza somando cada percentual de nível de cinza até um determinado nível de cinza k. Assim, se fossemos iniciar o cálculo do valor equalizado do nível de cinza 2, teríamos que somar o percentual do nível de cinza 0, nível de cinza 1 e nível de cinza 2, pois k = 2. 

Após isso, devemos arredondar o valor resultante dessa soma para um múltiplo de 1/*escala de cinza da imagem*, a fim de obter para qual nível de cinza todos os pixels do nível de cinza k serão remapeados. Retomando o exemplo do nível de cinza 2, se o resultado da soma arredondado para um múltiplo de 1/*escala de cinza da imagem* der como resultado o nível de cinza 5, por exemplo, cada pixel que possuía tonalidade de cinza 2 na imagem original terá agora o tom de cinza 5. 

Assim, realizando esse processo para cada tom de cinza presente na escala de cinza da imagem, obtemos um histograma equalizado da imagem.

A figura apresenta um exemplo de aplicação da técnica de equalização de histograma para aumentar o contraste de uma imagem 446 x 297 com 256 tons de cinza. A parte (a) apresenta a imagem original, cujo histograma é plotado na figura (c). A parte (d) mostra o histograma equalizado, correspondente à imagem da (b).

<img src="/src/assets/equalizacao-exemplo.png">

Além disso, podemos aplicar as técnicas de equalização de histogramas apenas em certos trechos da imagem também, como em janelas m x n de pixels. Estas técnicas locais servem principalmente para realçar detalhes sutis de pequenas porções da imagem.

## Especificação Direta de Histograma

## Definição

Apesar de sua grande utilização em situações de aprimoramento de contraste de imagens, a equalização de histograma apresenta como principal limitação o fato de não permitir a especificação de nenhum parâmetro de mudança capazes de ressaltar faixas de níveis de cinza na imagem. 

Ou seja, a equalização de histogramas procura apenas distribuir igualmente os tons de cinza para todos os níveis de pixels da imagem através da função de distribuição acumulada, sem parâmetros além dessa função para apontarem um histograma ideal para um determinado contexto.

Assim, seria desejável poder especificar que tipo de mudança se deseja sobre o histograma. Nestes casos, uma das possíveis técnicas é a especificação direta de histograma.

!<img src="/src/assets/especificacao-direta-exemplo1.png">

A figura apresenta um exemplo de aplicação da técnica de especificação direta de histograma aplicada a uma imagem 443 x 298 com 256 tons de cinza. A figura (a) apresenta a imagem original, cujo histograma é plotado na figura (c). A figura (d) mostra o histograma desejado, enquanto a figura (e) mostra o histograma obtido, que corresponde à imagem da figura (b).

!<img src="/src/assets/especificacao-direta-exemplo2.png">

## Procedimento

Dada uma imagem (e seu histograma original) e o novo histograma desejado, o procedimento da especificação direta de histograma consiste em realizar a equalização tanto no histograma original quanto no histograma desejado e comparar cada valor obtido na equalização do histograma original com os valores resultantes da equalização do histograma desejado. 

Depois disso, a comparação que tiver a menor diferença absoluta entre os valores fará com que todo pixel de tonalidade de cinza x que foi translocado para uma tonalidade de cinza y após a sua equalização mude para uma tonalidade de cinza z, o qual será o valor equalizado do histograma ideal pelo qual a tonalidade de cinza equalizada y se aproximou. 

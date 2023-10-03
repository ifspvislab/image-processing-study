# **Resumo: Realce de imagens no domínio espacial**

Nesta seção do livro "Processamento Digital de Imagens" de Marques Filho e Vieira Neto, são abordados os tópicos sobre o realce de imagens no domínio espacial.

O principal objetivo das técnicas de realce é o de destacar detalhes finos na imagem.

## **Filtro passa-altas básico**

Deve-se possuir uma máscara com coeficientes positivos nas proximidades de seu centro e negativos longe dele. Um exemplo é uma máscara 3x3, em que o seu pixel central deve ser positivo e todos seus oito vizinhos negativos.

![filtro](./assets/foto_passa_altas.png)

## **Realce por diferenciação**

O cálculo da média dos pixels em um trecho de imagem produz como efeito a remoção de seus componentes de alta frequência e o conceito de média é análogo à operação de integração, logo, a diferenciação irá enfatizar os componentes de alta frequência presentes numa imagem.

O método mais usual de diferenciação em aplicações de processamento de imagens é o gradiente. O gradiente de f(x,y) em um certo ponto (x,y) é definido como o vetor:

![filtro 2](./assets/foto_realce_por_diferenciacao.png)

A magnitude deste vetor é dada por: 

![filtro 3](./assets/foto_realce_por_diferenciacao2.png)

## **Filtragem high-boost**

A filtragem passa-altas também pode ser obtida subtraindo de uma imagem original uma versão filtrada por um filtro passa-baixas. Assim sendo, o filtro high-boost é uma extensão dessa ideia, ou seja, a imagem original é multiplicada por um fator de amplificação A: 

![filtro 4](./assets/foto_filtragem_high_boost.png)

Se A = 1, o filtro se comporta de forma idêntica a um passa-altas. 
Se A > 1, parte da imagem original é adicionada ao resultado, restaurando parcialmente os componentes de baixa frequência. O resultado é uma imagem que se parece com a original, com um grau relativo de realce das bordas, dependente do valor de A.

Exemplo de máscara utilizado para filtragem high-boost:

![filtro 5](./assets/foto_filtragem_high_boost2.png)
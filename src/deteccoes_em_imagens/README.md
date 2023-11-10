# **Resumo: Detecção de pontos isolados, linhas e bordas**

Nesta seção do livro "Processamento Digital de Imagens" de Marques Filho e Vieira Neto, são abordados os tópicos sobre detecção de pontos isolados, linhas e bordas 

## **Detecção de pontos isolados**

A seguinte máscara é um exemplo de operador de convolução que, quando aplicado a uma imagem, destacará pixels brilhantes circundados por pixels mais escuros. É conhecido por filtro passa-altas.

![filtro](./assets/passa-altas.png)

## **Detecção de linhas**

As máscaras a seguir podem ser utilizadas para a detecção de linhas horizontais e verticais (acima) e diagonais (abaixo).

![filtro 2](./assets/detecta-linhas.png)

## **Detecção de bordas**

Define-se **borda como a fronteira entre duas regiões cujos níveis de cinza predominantes são razoavelmente diferentes.** Podem-se definir bordas de textura e bordas de cor em imagens onde texturas ou a cor, respectivamente, são as mais importantes, mas aqui apenas são tratadas bordas de luminosidade. Para detecção de bordas, são usadas as seguintes máscaras:

![filtro 3](./assets/detecta-bordas.png)

Existe também o **operador laplaciano**, que é definido por:

![operador laplaciano](./assets/laplaciano.png)

E suas máscaras podem ser definidas por:

![mascara laplaciana](./assets/laplaciano-máscara.png)

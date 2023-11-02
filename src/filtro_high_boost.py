from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from utils import aplicar_filtro_Fimagem
from filtro_passa_ideal import filtro_passa_ideal


def high_boost(image: np.ndarray, lowpass_filtered_image: np.ndarray, A: float) -> np.ndarray:
    """
    Aplique a técnica de aprimoramento de alta frequência (high-boost) a uma imagem.

    Args:
        image (numpy.ndarray): A imagem original.
        lowpass_filtered_image (numpy.ndarray): A imagem filtrada pelo filtro passa-baixa.
        A (float): O fator de amplificação.

    Returns:
        Image: A imagem resultante após a aplicação do realce de alta frequência.

    Notes:
        A técnica de realce de alta frequência (high-boost) envolve a multiplicação da
        imagem original por um fator de amplificação (A) e a subtração da imagem filtrada
        pelo filtro passa-baixa. O resultado é uma imagem realçada, enfatizando as altas
        frequências.
    """
    result = A * image - lowpass_filtered_image
    return result


if __name__ == "__main__":
    imagem = Image.open("images/imagem_teste_filtros.jpg").convert("L")
    imagem_array = np.array(imagem)

    frequencias = [1.2, 5, 10, 15, 50, 100]

    plt.figure(figsize=(len(frequencias)*3, 3))
    plt.suptitle("Imagens filtradas com diferentes frequências de corte")

    for index, D0 in enumerate(frequencias):
        plt.subplot(1, len(frequencias), index+1)
        plt.title(f'D0={D0}')
        plt.axis('off')
        i_filtro = filtro_passa_ideal(imagem_array, D0, True)
        i_imagem = aplicar_filtro_Fimagem(imagem_array, i_filtro)
        hb_imagem = high_boost(imagem_array, i_imagem, 2)
        plt.imshow(hb_imagem, cmap='gray')

    plt.show()

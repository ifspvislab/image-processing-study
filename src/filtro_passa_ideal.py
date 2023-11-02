from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from utils import aplicar_filtro_Fimagem, distancia_dominio_frequencia


def filtro_passa_ideal(image: np.ndarray, D0: float, passa_baixa: bool = False) -> np.ndarray:
    """
    Cria um filtro ideal no domínio de frequência.

    Args:
        img (numpy.ndarray): A imagem de entrada.
        D0 (float): A frequência de corte do filtro ideal.
        lowpass (bool): Define se o filtro é passa-baixas (True) ou passa-altas (False).

    Returns:
        numpy.ndarray: O filtro ideal no domínio de frequência.

    Notes:
        Esta função cria um filtro ideal no domínio de frequência com base na
        frequência de corte D0 e na opção de filtro passa-baixas ou passa-altas.
        O filtro é retornado como uma matriz que pode ser usada para filtrar a imagem.
    """

    D = distancia_dominio_frequencia(image)

    if passa_baixa:
        L = np.heaviside(-1 * (D - D0), 1)
        return L
    else:
        H = np.heaviside(1 * (D - D0), 1)
        return H


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
        filtro = filtro_passa_ideal(imagem_array, D0, True)
        if_imagem = aplicar_filtro_Fimagem(imagem_array, filtro)
        plt.imshow(if_imagem, cmap='gray')

    plt.show()

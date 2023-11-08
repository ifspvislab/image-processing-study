from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from utils import aplicar_filtro_Fimagem, distancia_dominio_frequencia


def filtro_butterWorth(imagem: np.ndarray, D0: float, n: int, passa_baixa: bool = True) -> np.ndarray:
    """
    Cria um filtro Butterworth no domínio de frequência.

    Args:
        img (numpy.ndarray): A imagem de entrada.
        D0 (float): A frequência de corte do filtro Butterworth.
        n (int): A ordem do filtro Butterworth.
        lowpass (bool): Define se o filtro é passa-baixas (True) ou passa-altas (False).

    Returns:
        numpy.ndarray: O filtro Butterworth no domínio de frequência.

    Notes:
        Esta função cria um filtro Butterworth no domínio de frequência com base
        na frequência de corte D0, na ordem n e na opção de filtro passa-baixas ou passa-altas.
        O filtro é retornado como uma matriz que pode ser usada para filtrar a imagem.
    """
    D = distancia_dominio_frequencia(imagem)

    if passa_baixa:
        L = 1 / (1 + (D / D0) ** (2 * n))
        return L
    else:
        D = np.heaviside(D, 0.1) - np.sign(D) + D
        H = 1 / (1 + (D0 / D) ** (2 * n))
        return H


if __name__ == "__main__":
    imagem = Image.open("src/assets/imagem_teste_filtros.jpg").convert("L")
    imagem_array = np.array(imagem)

    frequencias = [5, 15, 30, 80]
    ordens = [1, 2, 3]

    plt.figure(figsize=(len(ordens)*3, len(frequencias)*3))
    plt.suptitle(
        "Imagens filtradas com diferentes frequências de corte e ordens")

    for row, D0 in enumerate(frequencias):
        for col, n in enumerate(ordens):
            plt.subplot(len(frequencias),
                        len(ordens),
                        row*len(ordens)+col+1)
            plt.title(f'D0={D0},n={n}')
            plt.axis('off')
            bw_filtro = filtro_butterWorth(imagem_array, D0, n, True)
            bwf_imagem = aplicar_filtro_Fimagem(imagem_array, bw_filtro)
            plt.imshow(bwf_imagem, cmap='gray')

    plt.show()

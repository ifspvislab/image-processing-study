import numpy as np
from PIL import Image
from utils import apply_filter

def homomorphic_filter(image: np.ndarray, D0: float = 20, n: int = 2, a: float = 0.5, b: float = 1.5) -> np.ndarray:
    """
    Aplica um filtro homomórfico a uma imagem no domínio da frequência.

    Args:
        img (numpy.ndarray): A imagem de entrada no domínio espacial.
        D0 (float): A frequência de corte do filtro homomórfico.
        n (int): Ordem do filtro homomórfico.
        a (float): Parâmetro de ênfase de baixas frequências.
        b (float): Parâmetro de ênfase de altas frequências.

    Returns:
        numpy.ndarray: O filtro homomórfico no domínio da frequência.

    Notes:
        O filtro homomórfico é usado para realçar as características de uma imagem no domínio da frequência.
        Ele calcula as coordenadas das frequências no domínio da frequência a partir das dimensões da imagem.
        Em seguida, calcula a distância no domínio da frequência e cria o filtro homomórfico com base nos parâmetros
        especificados (D0, n, a, b). O filtro homomórfico resultante é retornado no domínio da frequência.
    """
    # Definir o centro da imagem
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2

    # Calcular as coordenadas das frequências no domínio da frequência
    r, c = np.ogrid[0:rows, 0:cols]
    r -= center_row
    c -= center_col

    # Calcular a distância no domínio da frequência
    D = np.sqrt(r**2 + c**2)

    # Calcular o filtro homomórfico
    H = (b - a) * (1 - np.exp(-D**2 / (2 * D0**2))) + a
    
    return H


if __name__ == "__main__":
    imagem = Image.open("images/3.jpg").convert("L")
    imagem_array = np.array(imagem)
    filtro = homomorphic_filter(imagem_array)
    imagem_filtro = apply_filter(imagem_array, filtro)
    Image.fromarray(imagem_filtro).show()
    # imagem_filtro.save("images/3-filter-butter.png")
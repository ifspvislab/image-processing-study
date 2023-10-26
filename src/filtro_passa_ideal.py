from PIL import Image
import numpy as np
from utils import apply_filter

def ideal_filter(image: np.ndarray, D0: float, lowpass: bool = True) -> np.ndarray:
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
    row, col = image.shape
    rowsIndex = np.zeros((row, col))
    colsIndex = np.zeros((row, col))
    
    if row == col:
        for i in range(row):
            for j in range(col):
                rowsIndex[i, j] = i
        colsIndex = rowsIndex.T
    else:
        for i in range(row):
            for j in range(col):
                rowsIndex[i, j] = i 
                colsIndex[i, j] = j
    
    D = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            D[i, j] = np.sqrt(pow((rowsIndex[i, j] - row // 2), 2) + pow((colsIndex[i, j] - col // 2), 2))
    
    if lowpass:
        L = np.heaviside(-1 * (D - D0), 1)
        return L
    else:
        H = np.heaviside(1 * (D - D0), 1)
        return H

if __name__ == "__main__":
    imagem = Image.open("images/3.jpg").convert("L")
    imagem_array = np.array(imagem)
    filtro = ideal_filter(imagem_array, 20, 2)
    imagem_filtro = apply_filter(imagem_array, filtro)
    Image.fromarray(imagem_filtro).show()
    # imagem_filtro.save("images/3-filter-butter.png")

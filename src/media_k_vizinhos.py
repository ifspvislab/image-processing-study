from PIL import Image
import numpy as np
from utils import cell_neighbors


def k_nearest_numbers(array: np.ndarray, value: float, k: int):
    """
    Retorna os k números mais próximos a um valor em um vetor.

    Args:
        vetor (numpy.ndarray): O vetor de entrada.
        valor: O valor de referência.
        k (int): O número de vizinhos a serem selecionados.

    Returns:
        numpy.ndarray: Um array contendo os k números mais próximos ao valor.
    """
    # Calcula as diferenças absolutas entre o valor escolhido e os elementos do vetor
    differences = np.abs(array - value)

    # Cria um índice ordenado dos elementos do vetor com base nas diferenças
    sorted_indices = np.argsort(differences)

    # Seleciona os primeiros k índices ordenados
    k_nearest_indices = sorted_indices[:k]

    # Obtém os k números mais próximos usando os índices selecionado
    nearest_numbers = array[k_nearest_indices]

    return nearest_numbers


def k_neighbors_mean_filter(image: Image, window_size: int, k_neighbors: int) -> Image:
    """
    Aplica um filtro de média baseado nos k vizinhos mais próximos a cada pixel da imagem.

    Args:
        image (Image): A imagem de entrada.
        window_size (int): O tamanho da janela para selecionar vizinhos.
        k_neighbors (int): O número de vizinhos a serem considerados para calcular a média.

    Returns:
        Image: A imagem filtrada.

    Notes:
        Esta função calcula a média dos k vizinhos mais próximos a cada pixel da imagem,
        usando uma janela de tamanho especificado para definir a vizinhança.
    """
    image_array = np.array(image)
    row, col = image_array.shape
    for i in range(row):
        for j in range(col):
            neighbors = cell_neighbors(image_array, i, j, window_size)
            close_neighbors = k_nearest_numbers(
                neighbors, image_array[i][j], k_neighbors)
            new_value = sum(close_neighbors) / len(close_neighbors)
            image_array[i][j] = new_value

    return Image.fromarray(image_array)


if __name__ == "__main__":
    imagem = Image.open("images/qd3.png").convert("L")
    imagem_filtro = k_neighbors_mean_filter(imagem, 2, 3)
    imagem_filtro.show()
    imagem_filtro.save("images/3-qd3-filter-media-K.png")

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from utils import vizinhos_celula
from filtro_media import filtro_media


def k_proximos_valor(array: np.ndarray, value: float, k: int):
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
    diferencas = np.abs(array - value)

    # Cria um índice ordenado dos elementos do vetor com base nas diferenças
    indices_ordenados = np.argsort(diferencas)

    # Seleciona os primeiros k índices ordenados
    indices_proximos_k = indices_ordenados[:k]

    # Obtém os k números mais próximos usando os índices selecionado
    proximos = array[indices_proximos_k]

    return proximos


def filtro_media_k_vizinhos_proximos(image: np.ndarray, kernel: int, k_neighbors: int) -> np.ndarray:
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
    window_size = kernel//2

    linhas, colunas = image.shape

    for i in range(linhas):
        for j in range(colunas):
            vizinhos = vizinhos_celula(image, i, j, window_size)
            vizinhos_proximos = k_proximos_valor(
                vizinhos, image[i, j], k_neighbors)
            image[i, j] = np.mean(vizinhos_proximos)

    return image


if __name__ == "__main__":
    imagem = Image.open("src/assets/imagem_ruido.jpg").convert("L")
    imagem_array = np.array(imagem)
    
    k_vizinhos = [5, 15, 25]
    janela = 5

    plt.figure(figsize=(len(k_vizinhos)*3.6, 4))
    plt.suptitle("Imagens com Filtro Media K Vizinhos")

    plt.subplot(1, len(k_vizinhos)+2, 1)
    plt.title(f'Imagem Original')
    plt.axis('off')
    plt.imshow(imagem_array, cmap='gray')

    fmedia_imagem = filtro_media(imagem_array, janela)

    plt.subplot(1, len(k_vizinhos)+2, 2)
    plt.title(f'Imagem com filtro média')
    plt.axis('off')
    plt.imshow(fmedia_imagem, cmap='gray')

    for index, k in enumerate(k_vizinhos):
        plt.subplot(1, len(k_vizinhos)+2, index+3)
        plt.title(f'Janela={janela},k_vizinhos={k}')
        plt.axis('off')
        knmf_imagem = filtro_media_k_vizinhos_proximos(imagem_array, janela, k)
        plt.imshow(knmf_imagem, cmap='gray')

    plt.show()

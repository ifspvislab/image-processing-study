from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from utils import vizinhos_celula


def filtro_media(imagem: np.ndarray, kernel: int) -> np.ndarray:
    """
    Aplica um filtro de média a uma imagem.

    Args:
        imagem (numpy.ndarray): A imagem de entrada.
        kernel (int): Tamanho do kernel (janela) usado para calcular a média.

    Returns:
        numpy.ndarray: A imagem filtrada pela média.

    Notes:
        Esta função aplica um filtro de média à imagem de entrada. O tamanho do kernel
        é especificado pelo argumento 'kernel'. A imagem de saída é a imagem original
        após a aplicação do filtro de média.
    """
    window_size = kernel // 2

    linhas, colunas = imagem.shape
    for i in range(linhas):
        for j in range(colunas):
            # Obtém os valores dos vizinhos da célula atual
            vizinhos = vizinhos_celula(imagem, i, j, window_size)
            
            # Calcula a média dos valores dos vizinhos e atualiza a célula atual
            imagem[i, j] = np.mean(vizinhos)

    # Retorna a imagem após a aplicação do filtro de média
    return imagem


if __name__ == "__main__":
    imagem = Image.open("src/assets/imagem_ruido.jpg").convert("L")
    imagem_array = np.array(imagem)

    kernel = [3, 5, 7, 9]

    plt.figure(figsize=(len(kernel)*3.6, 4))
    plt.suptitle("Imagens com Filtro Media")

    plt.subplot(1, len(kernel)+1, 1)
    plt.title(f'Imagem Original')
    plt.axis('off')
    plt.imshow(imagem_array, cmap='gray')

    for index, k in enumerate(kernel):
        plt.subplot(1, len(kernel)+1, index+2)
        plt.title(f'Kernel={k}')
        plt.axis('off')
        mf_imagem = filtro_media(imagem_array, k)
        plt.imshow(mf_imagem, cmap='gray')

    plt.show()
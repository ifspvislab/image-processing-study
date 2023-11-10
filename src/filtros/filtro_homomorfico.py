import numpy as np
from numpy.fft import fft2, fftshift
from PIL import Image
import matplotlib.pyplot as plt

def filtro_homomorfico(imagem, alpha=0.7, beta=1.3, cutoff=32):
    """
    Aplica um filtro homomórfico a uma imagem.

    Args:
        imagem (numpy.ndarray): A imagem de entrada.
        alpha (float): Parâmetro de ganho do filtro homomórfico.
        beta (float): Parâmetro de nitidez do filtro homomórfico.
        cutoff (int): Frequência de corte do filtro homomórfico.

    Returns:
        numpy.ndarray: A imagem filtrada pelo filtro homomórfico.

    Notes:
        Esta função aplica um filtro homomórfico à imagem de entrada. O filtro é aplicado
        no domínio da frequência para realçar as informações de baixa e alta frequência
        da imagem. Os parâmetros alpha, beta e cutoff controlam o comportamento do filtro.
    """
    imagem = imagem.astype(np.float32)
    
    log_imagem = np.log1p(imagem)

    espectro = fft2(log_imagem)
    espectro = fftshift(espectro)

    linhas, colunas = imagem.shape
    centro_x, centro_y = linhas // 2, colunas // 2
    x = np.arange(colunas) - centro_x
    y = np.arange(linhas) - centro_y
    X, Y = np.meshgrid(x, y)
    D = np.sqrt(X ** 2 + Y ** 2)
    H = (1 - np.exp(-beta * (D ** 2 / (cutoff ** 2)))) * alpha + 1

    espectro_filtrado = espectro * H
    espectro_filtrado = np.fft.ifftshift(espectro_filtrado)
    log_imagem_filtrado = np.fft.ifft2(espectro_filtrado)
    imagem_filtrada = np.exp(np.real(log_imagem_filtrado))
    imagem_filtrada = (imagem_filtrada - np.min(imagem_filtrada)) / (np.max(imagem_filtrada) - np.min(imagem_filtrada)) * 255

    return imagem_filtrada.astype(np.uint8)

if __name__ == "__main__":
    imagem = Image.open("src/assets/imagem_homo.jpg").convert("L")
    imagem_array = np.array(imagem)

    imagem_filtrada = filtro_homomorfico(imagem_array)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Imagem Original")
    plt.imshow(imagem, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title("Imagem Filtrada")
    plt.imshow(imagem_filtrada, cmap='gray')
    plt.axis('off')
    plt.show()

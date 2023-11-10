import numpy as np
from numpy.lib.stride_tricks import as_strided
from numpy.fft import fft2, fftshift, ifft2, ifftshift


def janela_deslizante(arr, window_size):
    """
    Constrói uma visualização de janela deslizante da matriz.

    Args:
        arr (numpy.ndarray): A matriz de entrada.
        window_size (int): O tamanho da janela deslizante.

    Returns:
        numpy.ndarray: Uma visualização de janela deslizante da matriz.

    Notes:
        Esta função constrói uma visualização de janela deslizante da matriz
        de entrada, permitindo a extração de submatrizes sobrepostas de acordo
        com o tamanho da janela especificada.
    """
    arr = np.asarray(arr)
    window_size = int(window_size)
    if arr.ndim != 2:
        raise ValueError("Necessita de uma entrada 2-D")
    if not (window_size > 0):
        raise ValueError("Necessita de um tamanho de janela positivo")
    shape = (arr.shape[0] - window_size + 1,
             arr.shape[1] - window_size + 1,
             window_size, window_size)
    if shape[0] <= 0:
        shape = (1, shape[1], arr.shape[0], shape[3])
    if shape[1] <= 0:
        shape = (shape[0], 1, shape[2], arr.shape[1])
    strides = (arr.shape[1] * arr.itemsize, arr.itemsize,
               arr.shape[1] * arr.itemsize, arr.itemsize)
    return as_strided(arr, shape=shape, strides=strides)


def vizinhos_celula(arr, i, j, d):
    """
    Retorna os vizinhos da célula (i, j) até uma distância d.

    Args:
        arr (numpy.ndarray): A matriz de entrada.
        i (int): Coordenada x da célula.
        j (int): Coordenada y da célula.
        d (int): Distância máxima até os vizinhos.

    Returns:
        numpy.ndarray: Um array unidimensional contendo os vizinhos da célula.

    Notes:
        Esta função retorna os vizinhos da célula (i, j) até uma distância d,
        considerando a matriz de entrada. Ela usa a função `sliding_window` para
        criar uma janela deslizante e, em seguida, extrai os vizinhos dentro dessa
        janela.
    """
    w = janela_deslizante(arr, 2*d+1)

    ix = np.clip(i - d, 0, w.shape[0]-1)
    jx = np.clip(j - d, 0, w.shape[1]-1)

    i0 = max(0, i - d - ix)
    j0 = max(0, j - d - jx)
    i1 = w.shape[2] - max(0, d - i + ix)
    j1 = w.shape[3] - max(0, d - j + jx)

    return w[ix, jx][i0:i1, j0:j1].ravel()


def aplicar_filtro_Fimagem(image: np.ndarray, H: np.ndarray) -> np.ndarray:
    """
    Aplica um filtro no domínio de Fourier a uma imagem.

    Args:
        img (numpy.ndarray): A imagem de entrada (escala de cinza).
        H (numpy.ndarray): O filtro no domínio de frequência.

    Returns:
        numpy.ndarray: A imagem filtrada.

    Notes:
        Esta função aplica um filtro no domínio de Fourier à imagem de entrada.
        Primeiro, ela centraliza a imagem no domínio da frequência. Em seguida, aplica
        a Transformada de Fourier à imagem para converter a imagem para o domínio da frequência.
        Depois, multiplica a imagem no domínio da frequência pelo filtro especificado (H).
        Por fim, a função realiza a Transformada Inversa de Fourier para obter a imagem
        filtrada no domínio espacial.

    Args:
        img (numpy.ndarray): A imagem de entrada em escala de cinza.
        H (numpy.ndarray): O filtro no domínio de frequência a ser aplicado.

    Returns:
        numpy.ndarray: A imagem filtrada no domínio espacial.

    """
    # Aplica a Transformada de Fourier à imagem
    img_fourier = fftshift(fft2(image))

    # Aplica o filtro no domínio de Fourier
    filtro_em_fourier = img_fourier * H

    # Realiza a Transformada Inversa de Fourier para obter a imagem filtrada
    imagem_filtrada = np.real(ifft2(ifftshift(filtro_em_fourier)))

    return imagem_filtrada


def distancia_dominio_frequencia(image: np.ndarray) -> np.ndarray:
    linha, coluna = image.shape
    indices_linhas = np.zeros((linha, coluna))
    indices_colunas = np.zeros((linha, coluna))

    if linha == coluna:
        for i in range(linha):
            for j in range(coluna):
                indices_linhas[i, j] = i
        indices_colunas = indices_linhas.T
    else:
        for i in range(linha):
            for j in range(coluna):
                indices_linhas[i, j] = i
                indices_colunas[i, j] = j

    D = np.zeros((linha, coluna))
    for i in range(linha):
        for j in range(coluna):
            D[i, j] = np.sqrt(pow((indices_linhas[i, j] - linha // 2),
                              2) + pow((indices_colunas[i, j] - coluna // 2), 2))

    return D

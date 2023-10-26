from PIL import Image
import numpy as np
from utils import apply_filter
from filtro_passa_ideal import ideal_filter

def high_boost(image: np.ndarray, lowpass_filtered_image: np.ndarray, A: float) -> Image:
    """
    Apply the high-frequency enhancement technique (high-boost) to an image.

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
    return Image.fromarray(result)


if __name__ == "__main__":
    imagem = Image.open("images/3.jpg").convert("L")
    imagem_array = np.array(imagem)
    filtro = ideal_filter(imagem_array, 20, 2)
    imagem_passa = apply_filter(imagem_array, filtro)
    imagem = high_boost(imagem_array, imagem_passa, 2)
    imagem.show()
    # imagem_filtro.save("images/3-filter-butter.png")

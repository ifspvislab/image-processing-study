from PIL import Image, ImageFilter
import matplotlib.pyplot as plt 

def deteccao_linhas(image):
    # Cria a mascara
    mascara_horizontal = ImageFilter.Kernel((3, 3), [-1, -1, -1, 2, 2, 2, -1, -1, -1], scale=1)
    mascara_vertical = ImageFilter.Kernel((3, 3), [-1, 2, -1, -1, 2, -1, -1, 2, -1], scale=1)
    mascara_diagonal_ascendente = ImageFilter.Kernel((3, 3), [-1, -1, 2, -1, 2, -1, 2, -1, -1], scale=1)
    mascara_diagonal_descendente = ImageFilter.Kernel(
        (3, 3), [2, -1, -1, -1, 2, -1, -1, -1, 2], scale=1
    )

    # Aplica as mascaras
    imagem_linhas_horizontais = image.filter(mascara_horizontal)
    imagem_linhas_verticais = image.filter(mascara_vertical)
    imagem_linhas_diagonais_ascendentes = image.filter(mascara_diagonal_ascendente)
    imagem_linhas_diagonais_descendentes = image.filter(mascara_diagonal_descendente)

    return (imagem_linhas_horizontais, imagem_linhas_verticais, imagem_linhas_diagonais_ascendentes, imagem_linhas_diagonais_descendentes)

if __name__ == "__main__":
    imagem = Image.open("src/assets/foto1.jpg").convert("L")

    imagens_deteccao_linhas = deteccao_linhas(imagem)

    # Exibe as imagens original e filtradas
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 5, 1)
    plt.imshow(imagem, cmap="gray")
    plt.title("Imagem original (cinza)")
    plt.axis("off")

    titles = ["Linhas Horizontais", "Linhas Verticais", "Diagonais Ascendentes", "Diagonais Descendentes"]

    for i in range(4):
        plt.subplot(1, 5, i + 2)
        plt.imshow(imagens_deteccao_linhas[i], cmap="gray")
        plt.title(titles[i])
        plt.axis("off")

    plt.show()

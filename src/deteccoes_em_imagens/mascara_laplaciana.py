from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def filtro_laplaciano(image):
    # Cria a máscara  de Laplaciano 3x3
    mascara_laplaciano = ImageFilter.Kernel((3, 3), [0, -1, 0, -1, 4, -1, 0, -1, 0], scale=1)

    imagem_filtrada = image.filter(mascara_laplaciano)

    return imagem_filtrada

if __name__ == "__main__":
    imagem = Image.open('src/assets/foto1.jpg').convert("L")

    imagem_laplaciano = filtro_laplaciano(imagem)

    # Exibe a imagem original e a imagem filtrada
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(imagem, cmap="gray")
    plt.title("Imagem original (cinza)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(imagem_laplaciano, cmap="gray")
    plt.title("Filtro laplaciano")
    plt.axis("off")

    plt.show()

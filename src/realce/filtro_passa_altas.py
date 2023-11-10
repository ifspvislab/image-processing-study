from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def filtro_passa_altas(image):
    # Cria um filtro passa-alta simples
    mascara = ImageFilter.Kernel((3, 3), [-1, -1, -1, -1, 8, -1, -1, -1, -1], scale=1)

    imagem_filtrada = image.filter(mascara)

    return imagem_filtrada

if __name__ == "__main__":
    imagem = Image.open("src/assets/foto1.jpg").convert("L")

    # Aplica o filtro passa-alta
    imagem_passa_altas = filtro_passa_altas(imagem)

    # Exibe a imagem original e a imagem filtrada
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(imagem, cmap="gray")
    plt.title("Imagem original (cinza)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(imagem_passa_altas, cmap="gray")
    plt.title("Filtro passa-altas")
    plt.axis("off")

    plt.show()

from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def filtro_media(image):
    # Cria a mascara 3x3 do filtro da media
    mascara = ImageFilter.Kernel((3, 3), [1, 1, 1, 1, 1, 1, 1, 1, 1], scale=9)

    imagem_filtrada = image.filter(mascara)

    return imagem_filtrada


if __name__ == "__main__":
    imagem = Image.open("src/assets/foto1.jpg").convert("L")
   
    # Aplica o filtro da media
    imagem_media = filtro_media(imagem)

    # Exibe a imagem original e a imagem filtrada
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(imagem, cmap="gray")
    plt.title("Imagem original (cinza)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(imagem_media, cmap="gray")
    plt.title("Filtro da media")
    plt.axis("off")

    plt.show()

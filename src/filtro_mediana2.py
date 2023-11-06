from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def filtro_mediana(image):
    # Cria o tamanho do filtro da mediana
    raio = 3

    imagem_filtrada = image.filter(ImageFilter.MedianFilter(size=raio))

    return imagem_filtrada

if __name__ == "__main__":
    imagem = Image.open("assets/foto3.jpg").convert("L")
   
    # Aplica o filtro da media
    imagem_mediana = filtro_mediana(imagem)

    # Exibe a imagem original e a imagem filtrada
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(imagem, cmap="gray")
    plt.title("Imagem original (cinza)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(imagem_mediana, cmap="gray")
    plt.title("Filtro da mediana")
    plt.axis("off")

    plt.show()

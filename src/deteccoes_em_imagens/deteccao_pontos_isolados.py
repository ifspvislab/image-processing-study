from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def deteccao_pontos_isolados(image):
    # Cria a mascara 
    mascara = ImageFilter.Kernel((3, 3), [-1, -1, -1, -1, 8, -1, -1, -1, -1], scale=1)

    imagem_filtrada = image.filter(mascara)

    return imagem_filtrada

if __name__ == "__main__":
    imagem = Image.open("src/assets/foto1.jpg").convert("L")

    imagem_pontos_isolados = deteccao_pontos_isolados(imagem)

     # Exibe a imagem original e a imagem filtrada
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(imagem, cmap="gray")
    plt.title("Imagem original (cinza)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(imagem_pontos_isolados, cmap="gray")
    plt.title("Filtro para detecção em pontos isolados")
    plt.axis("off")

    plt.show()

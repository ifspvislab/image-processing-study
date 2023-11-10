from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def deteccao_bordas_sobel(image):
    # Cria as mascaras de Sobel 3X3
    mascara_horizontal = ImageFilter.Kernel((3, 3), [1, 0, -1, 2, 0, -2, 1, 0, -1], scale=1)
    mascara_vertical= ImageFilter.Kernel((3, 3), [-1, -2, -1, 0, 0, 0, 1, 2, 1], scale=1)

    # Aplica a convolução com as máscaras de Sobel
    gradiente_x = image.filter(mascara_horizontal)
    gradiente_y = image.filter(mascara_vertical)

    # Combina o gradiente_x e o gradiente_y para a obtencao da magnitude do gradiente
    imagem_borda = Image.new("L", image.size)
    pixels_borda = imagem_borda.load()
    pixels_x = gradiente_x.load()
    pixels_y = gradiente_y.load()

    largura, altura = image.size

    for x in range(largura):
        for y in range(altura):
            magnitude = int((pixels_x[x, y]**2 + pixels_y[x, y]**2)**0.5)
            pixels_borda[x, y] = magnitude

    return imagem_borda

if __name__ == "__main__":
    imagem = Image.open("src/assets/foto1.jpg").convert("L")

    imagem_deteccao_bordas_sobel = deteccao_bordas_sobel(imagem)

     # Exibe a imagem original e a imagem filtrada
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(imagem, cmap="gray")
    plt.title("Imagem original (cinza)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(imagem_deteccao_bordas_sobel, cmap="gray")
    plt.title("Filtro para detecção de bordas (Sobel)")
    plt.axis("off")

    plt.show()

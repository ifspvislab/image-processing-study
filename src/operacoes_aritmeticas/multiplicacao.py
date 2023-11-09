from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# Carregue as imagens
imagem1 = Image.open('assets/imagem1.jpg')
imagem2 = Image.open('assets/imagem2.jpg')

# Certifique-se de que as imagens tenham o mesmo tamanho
if imagem1.size != imagem2.size:
    raise ValueError("As imagens devem ter o mesmo tamanho.")

# Realize a multiplicação pixel a pixel
imagem_resultante = ImageChops.multiply(imagem1, imagem2)

# Exibindo as imagens
plt.figure(figsize=(10, 5))

# Subplot para a imagem 1
plt.subplot(1, 3, 1)
plt.imshow(imagem1)
plt.title('Imagem 1')
plt.axis('off')

# Subplot para a imagem 2
plt.subplot(1, 3, 2)
plt.imshow(imagem2)
plt.title('Imagem 2')
plt.axis('off')

# Subplot para a imagem resultante
plt.subplot(1, 3, 3)
plt.imshow(imagem_resultante)
plt.title('Imagem Resultante')
plt.axis('off')

# Exibindo os subplots
plt.tight_layout()
plt.show()
from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# Carregando as imagens
imagem1 = Image.open('src/assets/imagem1.jpg')
imagem2 = Image.open('src/assets/imagem2.jpg')

# Subtração de imagens (apenas para imagens em tons de cinza)
resultado_subtracao = ImageChops.subtract(imagem1, imagem2)

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
plt.imshow(resultado_subtracao)
plt.title('Imagem Resultante')
plt.axis('off')

# Exibindo os subplots
plt.tight_layout()
plt.show()
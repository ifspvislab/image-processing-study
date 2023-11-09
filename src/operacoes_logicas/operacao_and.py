from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# Carregando as imagens
imagem1 = Image.open('assets/imagem1.jpg')
imagem2 = Image.open('assets/imagem2.jpg')

# Converter as imagens para modo binário (1-bit)
imagem1_bin = imagem1.convert('1')
imagem2_bin = imagem2.convert('1')

# Operação AND
resultado_and = ImageChops.logical_and(imagem1_bin, imagem2_bin)

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
plt.imshow(resultado_and)
plt.title('Imagem Resultante')
plt.axis('off')

# Exibindo os subplots
plt.tight_layout()
plt.show()
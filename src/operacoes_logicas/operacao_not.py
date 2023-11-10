from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Carregue a imagem
imagem = Image.open('src/assets/imagem1.jpg')

# Certifique-se de que a imagem esteja no modo binário (1-bit)
imagem_bin = imagem.convert('1')

# Aplique a operação NOT
imagem_not = ImageOps.invert(imagem_bin)


# Exibindo as imagens
plt.figure(figsize=(10, 5))

# Subplot para a imagem 1
plt.subplot(1, 3, 1)
plt.imshow(imagem)
plt.title('Imagem 1')
plt.axis('off')

# Subplot para a imagem resultante
plt.subplot(1, 3, 3)
plt.imshow(imagem_not)
plt.title('Imagem Resultante')
plt.axis('off')

# Exibindo os subplots
plt.tight_layout()
plt.show()

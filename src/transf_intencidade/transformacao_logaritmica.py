import math
from PIL import Image
import matplotlib.pyplot as plt
import os

# Obtenha o caminho absoluto do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Combine o caminho do diretório atual com o caminho da imagem
caminho_imagem = os.path.join(diretorio_atual, '../../assets/imagem1.jpg')

img1 = Image.open(caminho_imagem)
img = Image.open(caminho_imagem)

matriz = img.load()

c = 255 / math.log(1 + 255)

for i in range(img.size[0]):
  for j in range(img.size[1]):
    r = c * math.log(1 + matriz[i,j][0])
    g = c * math.log(1 + matriz[i,j][1])
    b = c * math.log(1 + matriz[i,j][2])
    matriz[i,j] = (int(r),int(g),int(b))

# Cria uma figura com dois subplots
plt.figure(figsize=(10, 5))

# Subplot para a imagem original
plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.title('Imagem Original')
plt.axis('off')

# Subplot para a imagem processada
plt.subplot(1, 2, 2)
plt.imshow(img)
plt.title('Imagem Processada')
plt.axis('off')

# Exibe os subplots
plt.tight_layout()
plt.show()
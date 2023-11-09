from PIL import Image
import matplotlib.pyplot as plt
import os

# Obtenha o caminho absoluto do diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Combine o caminho do diretório atual com o caminho da imagem
caminho_imagem = os.path.join(diretorio_atual, '../../assets/imagem1.jpg')

# Abra a imagem
imagem = Image.open(caminho_imagem)

# Obtenha o histograma
histograma = imagem.histogram()

# Plote o histograma
plt.hist(histograma, bins=256, range=(0, 256), density=True, color='gray', alpha=0.7)
plt.title('Histograma de Imagem em Tons de Cinza')
plt.xlabel('Nível de Cinza')
plt.ylabel('Frequência Normalizada')
plt.show()

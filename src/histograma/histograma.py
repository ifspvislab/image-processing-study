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

# Divida o histograma nas bandas R, G e B
r_hist = histograma[0:256]
g_hist = histograma[256:512]
b_hist = histograma[512:768]

# Plote os histogramas
plt.figure(figsize=(10, 5))
plt.title('Histograma de Imagem')
plt.xlabel('Nível de Cinza')
plt.ylabel('Contagem')
plt.plot(r_hist, color='red', label='R')
plt.plot(g_hist, color='green', label='G')
plt.plot(b_hist, color='blue', label='B')
plt.legend()
plt.show()

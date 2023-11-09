from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def especificacao_histograma(imagem, histograma_alvo):
    # Converte a imagem Pillow para um array NumPy
    imagem_array_np = np.array(imagem)

    # Calcula o histograma da imagem de entrada
    histograma = np.histogram(imagem_array_np.flatten(), 256, [0, 256])[0]

    # Calcula a função de distribuição acumulativa (CDF) do histograma de entrada
    cdf = histograma.cumsum()

    # Normaliza a CDF para estar no intervalo [0, 1]
    cdf_normalizado = cdf / cdf.max()

    # Calcula a CDF do histograma alvo e o normaliza.
    cdf_alvo = histograma_alvo.cumsum()
    cdf_alvo_normalizado = cdf_alvo / cdf_alvo.max()

    # Mapeia os valores de intensidade de pixel usando a CDF
    valores_mapeados = np.interp(cdf_normalizado, cdf_alvo_normalizado, range(256))

    # Aplica a transformação aos pixels da imagem
    imagem_equalizada = np.interp(imagem_array_np.flatten(), range(256), valores_mapeados)

    # Remodela a imagem equalizada de volta ao formato original
    imagem_equalizada = imagem_equalizada.reshape(imagem_array_np.shape)

    # Converte o array NumPy de volta para uma imagem Pillow
    imagem_equalizada_pil = Image.fromarray(imagem_equalizada.astype(np.uint8))

    return imagem_equalizada_pil

# Carrega a imagem de entrada usando a Pillow e o converte para cinza.
imagem_entrada = Image.open('assets/passaro.png').convert('L')

# Define o histograma alvo desejado (pode ser obtido de outra imagem)
imagem_alvo = Image.open('assets/cidade.jpg').convert('L')
histograma_ideal = np.histogram(np.array(imagem_alvo).flatten(), 256, [0, 256])[0]

# Aplica a especificação direta de histograma
imagem_saida = especificacao_histograma(imagem_entrada, histograma_ideal)

# Mostra os histogramas
plt.subplot(131)
plt.plot(imagem_entrada.histogram())
plt.title("Histograma original")

plt.subplot(132)
plt.plot(imagem_alvo.histogram())
plt.title("Histograma alvo")

plt.subplot(133)
plt.plot(imagem_saida.histogram())

plt.suptitle("Histogramas da especificação direta de imagens")
plt.show()

# Mostra as imagens
plt.subplot(121).axis('off')
plt.imshow(imagem_entrada, cmap='gray')
plt.title('Imagem original')

plt.subplot(122).axis('off')
plt.imshow(imagem_saida, cmap='gray')
plt.title('Imagem especificada')

plt.show()
